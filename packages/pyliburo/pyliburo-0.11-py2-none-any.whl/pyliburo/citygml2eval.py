# ==================================================================================================
#
#    Copyright (c) 2016, Chen Kian Wee (chenkianwee@gmail.com)
#
#    This file is part of pyliburo
#
#    pyliburo is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    pyliburo is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with Dexen.  If not, see <http://www.gnu.org/licenses/>.
#
# ==================================================================================================
import os

import pycitygml
import py3dmodel
import gml3dmodel
import urbanformeval

class Evals(object):
    def __init__(self, citygmlfile):
        reader = pycitygml.Reader()
        reader.load_filepath(citygmlfile)
        self.citygml = reader
        self.citygmlfilepath = citygmlfile
        self.buildings = self.citygml.get_buildings()
        self.landuses = self.citygml.get_landuses()
        self.stops = self.citygml.get_bus_stops()
        self.roads = self.citygml.get_roads()
        self.railways = self.citygml.get_railways()
        self.relief_features = self.citygml.get_relief_feature()
        #occ geometries
        self.building_occsolids = None
        self.roof_occfaces = None
        self.facade_occfaces = None
        self.footprint_occfaces = None
        self.building_dictlist = None
        self.buildings_on_plot_2dlist = None #2d list of building dictlist according to the plot they belong to 
        self.landuse_occpolygons = None
        self.relief_feature_occshells = None
        self.relief_feature_occfaces = None
        self.road_occedges = None
        #radiance parameters
        self.rad_base_filepath = os.path.join(os.path.dirname(__file__),'py2radiance','base.rad')
        self.nshffai_folderpath = os.path.join(os.path.dirname(self.citygmlfilepath), 'nshffai_data')
        self.dffai_folderpath = os.path.join(os.path.dirname(self.citygmlfilepath), 'dffai_data')
        self.pvefai_folderpath = os.path.join(os.path.dirname(self.citygmlfilepath), 'pvefai_data')
        self.daysim_folderpath = os.path.join(os.path.dirname(self.citygmlfilepath), 'daysim_data')
        self.solarxdim = None
        self.solarydim = None
        self.rad = None
        #rad results 
        self.irrad_results = None
        self.illum_results = None
        self.facade_grid_srfs = None
        self.roof_grid_srfs = None
        
    def initialise_occgeom(self):
        buildings = self.buildings
        bsolid_list = []
        roof_list = []
        facade_list = []
        footprint_list = []
        building_dictlist = []
        for building in buildings:
            building_dict ={}
            #get all the polygons from the building 
            pypolygonlist = self.citygml.get_pypolygon_list(building) 
            bsolid = py3dmodel.construct.make_occsolid_frm_pypolygons(pypolygonlist)
            #extract the polygons from the building and separate them into facade, roof, footprint
            facades, roofs, footprints = gml3dmodel.identify_building_surfaces(bsolid)
            building_dict["facade"] = facades
            building_dict["footprint"] = footprints[0]
            building_dict["roof"] = roofs
            building_dict["solid"] = bsolid
            building_dictlist.append(building_dict)
            bsolid_list.append(bsolid)
            facade_list.extend(facades)
            roof_list.extend(roofs)
            footprint_list.extend(footprints)
            
        self.building_dictlist = building_dictlist
        self.building_occsolids = bsolid_list
        self.facade_occfaces = facade_list
        self.roof_occfaces = roof_list
        self.footprint_occfaces = footprint_list
        
        #get the relief feature
        relief_features = self.relief_features
        rf_occtriangle_list = []
        rf_shell_list = []
        for rf in relief_features:
            pytrianglelist = self.citygml.get_pytriangle_list(rf)
            occtriangle_list = []
            for pytriangle in pytrianglelist:
                occtriangle = py3dmodel.construct.make_polygon(pytriangle)
                rf_occtriangle_list.append(occtriangle)
                occtriangle_list.append(occtriangle)
            rf_shell = py3dmodel.construct.make_shell_frm_faces(occtriangle_list)[0]
            rf_shell_list.append(rf_shell)
            
        self.relief_feature_occfaces = rf_occtriangle_list
        self.relief_feature_occshells = rf_shell_list
        
        #get the roads
        roads = self.roads
        road_occedges = []
        for road in roads:
            polylines = self.citygml.get_pylinestring_list(road)
            for polyline in polylines:
                occ_wire = py3dmodel.construct.make_wire(polyline)
                edge_list = py3dmodel.fetch.geom_explorer(occ_wire, "edge")
                road_occedges.extend(edge_list)
                
        self.road_occedges = road_occedges
        
        #get the land-use plot
        landuses = self.landuses
        lface_list = []
        for landuse in landuses:
            lpolygons = self.citygml.get_polygons(landuse)
            if lpolygons:
                lfaces = []
                if len(lpolygons)>1:
                    for lpolygon in lpolygons:
                        landuse_pts = self.citygml.polygon_2_pt_list(lpolygon)
                        lface = py3dmodel.construct.make_polygon(landuse_pts)
                        lfaces.append(lface)
                    merged_face = py3dmodel.construct.merge_faces(lfaces)[0]
                if len(lpolygons)==1:
                    landuse_pts = self.citygml.polygon_2_pt_list(lpolygons[0])
                    lface = py3dmodel.construct.make_polygon(landuse_pts)
                    merged_face = lface
                    
                lface_list.append(merged_face)
                
        self.landuse_occpolygons = lface_list
        
    def nshffai(self, irrad_threshold, epwweatherfile, xdim, ydim, nshffai_threshold=None):
        """
        Solar Heat Gain Facade Area to Volume Index (SHGFAVI) calculates the ratio of facade area that 
        receives irradiation above a specified level over the building volume. 
        """
        if self.building_occsolids == None:
            self.initialise_occgeom()
            
        rf_occfaces = self.relief_feature_occfaces
        bsolid_list = self.building_occsolids
        result_dict = urbanformeval.nshffai(bsolid_list, irrad_threshold, epwweatherfile, xdim, ydim, self.nshffai_folderpath, 
                                            nshffai_threshold = nshffai_threshold, shading_occfaces = rf_occfaces)
        
        self.irrad_results = result_dict["solar_results"]
        return result_dict
        
    def dffai(self, illum_threshold, epwweatherfile, xdim, ydim, dffai_threshold=None):
        """
        Daylighting Facade Area to Volume Index (DFAI) calculates the ratio of facade area that 
        receives daylighting above a specified level, 
        over the building volume. 
        """ 
        if self.building_occsolids == None:
            self.initialise_occgeom()
            
        rf_occfaces = self.relief_feature_occfaces
        bsolid_list = self.building_occsolids
        result_dict = urbanformeval.dffai(bsolid_list, illum_threshold, epwweatherfile, xdim,ydim, self.dffai_folderpath, 
                                          self.daysim_folderpath, dffai_threshold = dffai_threshold, 
                                          shading_occfaces = rf_occfaces)

        self.illum_results = result_dict["solar_results"]
        return result_dict
        
    def pvafai(self, irrad_threshold, epwweatherfile, xdim, ydim, surface = "roof", pvafai_threshold = None):
        '''
        epv calculates the potential electricity 
        that can be generated on the roof of buildings annually.
        epv is represented in kWh/yr.
        
        PV Area to Volume Index (PVAVI) calculates the ratio of roof area that 
        receives irradiation above a specified level, 
        over the building volume. 
        '''
        if self.building_occsolids == None:
            self.initialise_occgeom()
            
        rf_occfaces = self.relief_feature_occfaces
        bsolid_list = self.building_occsolids
        result_dict = urbanformeval.pvafai(bsolid_list, irrad_threshold, epwweatherfile, xdim, ydim, self.pvefai_folderpath, 
                                          mode = surface, pvafai_threshold = pvafai_threshold, shading_occfaces = rf_occfaces )

        return result_dict
    
    def pvefai(self, roof_irrad_threshold, facade_irrad_threshold, epwweatherfile, xdim, ydim, 
               pvrfai_threshold = None, pvffai_threshold = None, pvefai_threshold = None):
        '''
        epv calculates the potential electricity 
        that can be generated on the roof of buildings annually.
        epv is represented in kWh/yr.
        
        PV Envelope Area to Volume Index (PVEAVI) calculates the ratio of roof area that 
        receives irradiation above a specified level, 
        over the building volume. 
        
        Same as PVAVI but runs it for the whole envelope 
        '''
        if self.building_occsolids == None:
            self.initialise_occgeom()
            
        rf_occfaces = self.relief_feature_occfaces
        bsolid_list = self.building_occsolids
        result_dict = urbanformeval.pvefai(bsolid_list, roof_irrad_threshold, facade_irrad_threshold, epwweatherfile, xdim, ydim, 
                                           self.pvefai_folderpath, pvrfai_threshold = pvrfai_threshold,
                                           pvffai_threshold = pvffai_threshold, pvefai_threshold = pvefai_threshold,
                                           shading_occfaces = rf_occfaces)
                                                                                             
        return result_dict

    def fai(self, wind_dir, boundary_occface = None):
        """
        Frontal Area Index (FAI)
        """
        
        if self.relief_feature_occshells == None:
            self.initialise_occgeom()
            
        
        if boundary_occface == None:
            rf_shells = self.relief_feature_occshells
            rf_compound = py3dmodel.construct.make_compound(rf_shells)
            xmin,ymin,zmin,xmax,ymax,zmax = py3dmodel.calculate.get_bounding_box(rf_compound)
            
            all_flatten_rf_faces = []
            for rfshell in rf_shells:
                rffaces = py3dmodel.fetch.geom_explorer(rfshell, "face")
                for rfface in rffaces:
                    #rf_nrml = py3dmodel.calculate.face_normal(rfface)
                    #ref_nrml = (0,0,1)
                    #print rf_nrml
                    #angle = py3dmodel.calculate.angle_bw_2_vecs(rf_nrml,ref_nrml)
                    #flatten the surfaces 
                    flatten_face_z = py3dmodel.modify.flatten_face_z_value(rfface, z = zmin)
                    all_flatten_rf_faces.append(flatten_face_z)         
            boundary_occface = py3dmodel.construct.merge_faces(all_flatten_rf_faces)[0]
            
        bsolid_list = self.building_occsolids
        print "ANALYSING FAI ..."
        res_dict = urbanformeval.frontal_area_index(bsolid_list, boundary_occface,wind_dir,xdim = 100, ydim = 100)
                                                                                                         
        return res_dict
        
    def rdi(self, boundary_occface = None, obstruction_occfacelist = [], rdi_threshold = 1.6):
        """
        Route Directness Index
        """
        if self.road_occedges == None:
            self.initialise_occgeom()
            
        #TODO: currently the function only works on flat terrain
        road_occedges = self.road_occedges
        plot_occfacelist = self.landuse_occpolygons
        if boundary_occface == None:
            rf_faces = self.relief_feature_occfaces
            compound_list = rf_faces + road_occedges + plot_occfacelist + obstruction_occfacelist
            compound = py3dmodel.construct.make_compound(compound_list)
            xmin,ymin,zmin,xmax,ymax,zmax = py3dmodel.calculate.get_bounding_box(compound)
            
            f_rf_face_list = []
            for rf_face in rf_faces:
                f_rf_face = py3dmodel.modify.flatten_face_z_value(rf_face, z = zmin)
                f_rf_face_list.append(f_rf_face)
                
            boundary_occface = py3dmodel.construct.merge_faces(f_rf_face_list)[0]
            
        if boundary_occface != None:
            compound_list = [boundary_occface] + road_occedges + plot_occfacelist + obstruction_occfacelist
            compound = py3dmodel.construct.make_compound(compound_list)
            xmin,ymin,zmin,xmax,ymax,zmax = py3dmodel.calculate.get_bounding_box(compound)
            
            boundary_occface = py3dmodel.modify.flatten_face_z_value(boundary_occface, z = zmin)
            
        f_redge_list = []
        road_length_list = []
        for redge in road_occedges:
            f_redge = py3dmodel.modify.flatten_edge_z_value(redge, z = zmin)
            lbound, ubound = py3dmodel.fetch.edge_domain(f_redge)
            edge_length = py3dmodel.calculate.edgelength(lbound, ubound, f_redge)
            road_length_list.append(edge_length)
            f_redge_list.append(f_redge)
            
        road_length = sum(road_length_list)
            
        f_p_face_list = []
        for p_face in plot_occfacelist:
            f_p_face = py3dmodel.modify.flatten_face_z_value(p_face, z = zmin)
            f_p_face_list.append(f_p_face)
            
        f_o_face_list = []
        for o_face in obstruction_occfacelist:
            f_o_face = py3dmodel.modify.flatten_face_z_value(o_face, z = zmin)
            f_o_face_list.append(f_o_face)
                
        res_dict = urbanformeval.route_directness(f_redge_list, f_p_face_list, boundary_occface,
                                                  obstruction_occfacelist = f_o_face_list,rdi_threshold = rdi_threshold)
        
        res_dict["road_length"] = road_length
                                                                                                        
        return res_dict


#===================================================================================================================================================