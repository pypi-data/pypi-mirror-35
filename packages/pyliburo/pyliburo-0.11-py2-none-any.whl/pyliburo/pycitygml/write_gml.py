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
import uuid
import datetime

from lxml.etree import Element, SubElement

class XMLNamespaces:
   citygml = "http://www.opengis.net/citygml/1.0"
   core = "http://www.opengis.net/citygml/base/1.0"
   xsi = "http://www.w3.org/2001/XMLSchema-instance"
   trans="http://www.opengis.net/citygml/transportation/1.0"
   wtr = "http://www.opengis.net/citygml/waterbody/1.0"
   gml = "http://www.opengis.net/gml"
   smil20lang = "http://www.w3.org/2001/SMIL20/Language"
   xlink = "http://www.w3.org/1999/xlink"
   grp = "http://www.opengis.net/citygml/cityobjectgroup/1.0"
   luse = "http://www.opengis.net/citygml/landuse/1.0"
   frn="http://www.opengis.net/citygml/cityfurniture/1.0"
   app="http://www.opengis.net/citygml/appearance/1.0"
   tex="http://www.opengis.net/citygml/texturedsurface/1.0"
   smil20="http://www.w3.org/2001/SMIL20/"
   xAL="urn:oasis:names:tc:ciq:xsdschema:xAL:2.0"
   bldg="http://www.opengis.net/citygml/building/1.0"
   dem="http://www.opengis.net/citygml/relief/1.0"
   veg="http://www.opengis.net/citygml/vegetation/1.0"
   gen="http://www.opengis.net/citygml/generics/1.0"

def write_root():
   schemaLocation="http://www.opengis.net/citygml/landuse/1.0\
                  http://schemas.opengis.net/citygml/landuse/1.0/landUse.xsd http://www.opengis.net/citygml/cityfurniture/1.0\
                  http://schemas.opengis.net/citygml/cityfurniture/1.0/cityFurniture.xsd http://www.opengis.net/citygml/appearance/1.0\
                  http://schemas.opengis.net/citygml/appearance/1.0/appearance.xsd http://www.opengis.net/citygml/texturedsurface/1.0\
                  http://schemas.opengis.net/citygml/texturedsurface/1.0/texturedSurface.xsd http://www.opengis.net/citygml/transportation/1.0\
                  http://schemas.opengis.net/citygml/transportation/1.0/transportation.xsd http://www.opengis.net/citygml/waterbody/1.0\
                  http://schemas.opengis.net/citygml/waterbody/1.0/waterBody.xsd http://www.opengis.net/citygml/building/1.0\
                  http://schemas.opengis.net/citygml/building/1.0/building.xsd http://www.opengis.net/citygml/relief/1.0\
                  http://schemas.opengis.net/citygml/relief/1.0/relief.xsd http://www.opengis.net/citygml/vegetation/1.0\
                  http://schemas.opengis.net/citygml/vegetation/1.0/vegetation.xsd http://www.opengis.net/citygml/cityobjectgroup/1.0\
                  http://schemas.opengis.net/citygml/cityobjectgroup/1.0/cityObjectGroup.xsd http://www.opengis.net/citygml/generics/1.0\
                  http://schemas.opengis.net/citygml/generics/1.0/generics.xsd"
   
   root = Element("CityModel",
               attrib={"{" + XMLNamespaces.xsi + "}schemaLocation" : schemaLocation},
               nsmap={None:"http://www.opengis.net/citygml/1.0",
                      'core': XMLNamespaces.core,
                      'xsi':XMLNamespaces.xsi,
                      'trans':XMLNamespaces.trans,
                      'wtr': XMLNamespaces.wtr,
                      'gml': XMLNamespaces.gml,
                      'smil20lang': XMLNamespaces.smil20lang,
                      'xlink': XMLNamespaces.xlink,
                      'grp': XMLNamespaces.grp,
                      'luse': XMLNamespaces.luse,
                      'frn': XMLNamespaces.frn,
                      'app': XMLNamespaces.app,
                      'tex': XMLNamespaces.tex,
                      'smil20': XMLNamespaces.smil20,
                      'xAL': XMLNamespaces.xAL,
                      'bldg': XMLNamespaces.bldg,
                      'dem': XMLNamespaces.dem,
                      'veg': XMLNamespaces.veg,
                      'gen': XMLNamespaces.gen})
   return root

def write_boundedby(parent_node, crs, lowercorner, uppercorner):
   gml_boundedBy = SubElement(parent_node, "{" + XMLNamespaces.gml+ "}" + 'boundedBy')
   #TO DO: implement geometry operattions to find the boundary
   gml_Envelope = SubElement(gml_boundedBy, "{" + XMLNamespaces.gml+ "}" + 'Envelope')
   gml_Envelope.attrib['srsName'] = crs
   gml_lowerCorner = SubElement(gml_Envelope, "{" + XMLNamespaces.gml+ "}" + 'lowerCorner')
   gml_lowerCorner.attrib['srsDimension'] = '3'
   gml_lowerCorner.text = str(lowercorner[0]) + " " +  str(lowercorner[1]) + " " + str(lowercorner[2]) 
   gml_upperCorner = SubElement(gml_Envelope, "{" + XMLNamespaces.gml+ "}" + 'upperCorner')
   gml_upperCorner.attrib['srsDimension'] = '3'
   gml_upperCorner.text = str(uppercorner[0]) + " " + str(uppercorner[1]) + " " + str(uppercorner[2]) 
   

def write_gen_Attribute(parent_node, generic_attrib_dict):
   for name in generic_attrib_dict:
      attrib = generic_attrib_dict[name]
      if type(attrib) == int:
         gen_intAttribute = SubElement(parent_node, "{" + XMLNamespaces.gen + "}" +'intAttribute')
         gen_intAttribute.attrib['name'] = name
         gen_value = SubElement(gen_intAttribute, "{" + XMLNamespaces.gen + "}" +'value')
         gen_value.text = str(attrib)
      
      if type(attrib) == float:
         gen_doubleAttribute = SubElement(parent_node, "{" + XMLNamespaces.gen + "}" +'doubleAttribute')
         gen_doubleAttribute.attrib['name'] = name
         gen_value = SubElement(gen_doubleAttribute, "{" + XMLNamespaces.gen + "}" +'value')
         gen_value.text = str(attrib)
         
      if type(attrib) == str:
         gen_stringAttribute = SubElement(parent_node, "{" + XMLNamespaces.gen + "}" +'stringAttribute')
         gen_stringAttribute.attrib['name'] = name
         gen_value = SubElement(gen_stringAttribute, "{" + XMLNamespaces.gen + "}" +'value')
         gen_value.text = str(attrib)

def write_landuse(lod, name, geometry_list, function = None, generic_attrib_dict = None):
   cityObjectMember = Element('cityObjectMember')

   luse = SubElement(cityObjectMember, "{" + XMLNamespaces.luse+ "}" +'LandUse')
   luse.attrib["{" + XMLNamespaces.gml+ "}" +'id'] = name

   gml_name = SubElement(luse, "{" + XMLNamespaces.gml+ "}" + 'name')
   gml_name.text = name
   
   #=======================================================================================================
   #attribs
   #=======================================================================================================
   if function != None:
       luse_function = SubElement(luse, "{" + XMLNamespaces.luse+ "}" +'function')
       luse_function.text = function
       
   if generic_attrib_dict != None:
       write_gen_Attribute(luse, generic_attrib_dict)

   #=======================================================================================================
   #geometries
   #=======================================================================================================
   if lod == "lod1":
      luse_lod1MultiSurface = SubElement(luse, "{" + XMLNamespaces.luse+ "}" + 'lod1MultiSurface')

      gml_MultiSurface = SubElement(luse_lod1MultiSurface, "{" + XMLNamespaces.gml+ "}" + 'MultiSurface')
      gml_MultiSurface.attrib["{" + XMLNamespaces.gml+ "}" +'id'] = 'UUID_' + str(uuid.uuid1())

      for geometry in geometry_list:
         gml_MultiSurface.append(geometry.construct())
      
   return cityObjectMember
   
def write_tin_relief(lod, name, geometry_list):
   cityObjectMember = Element('cityObjectMember')

   relief_feature = SubElement(cityObjectMember, "{" + XMLNamespaces.dem+ "}" +'ReliefFeature')
   relief_feature.attrib["{" + XMLNamespaces.gml+ "}" +'id'] = name

   gml_name = SubElement(relief_feature, "{" + XMLNamespaces.gml+ "}" + 'name')
   gml_name.text = name

   #=======================================================================================================
   #geometries
   #=======================================================================================================
   if lod == "lod1":
      dem_lod = SubElement(relief_feature, "{" + XMLNamespaces.dem+ "}" + 'lod')
      dem_lod.text = "1"
      dem_reliefComponent = SubElement(relief_feature, "{" + XMLNamespaces.dem+ "}" + 'reliefComponent')
      
      dem_TINRelief = SubElement(dem_reliefComponent, "{" + XMLNamespaces.dem+ "}" + 'TINRelief')
      dem_TINRelief.attrib["{" + XMLNamespaces.gml+ "}" +'id'] = name+"dem"
      
      gml_name = SubElement(dem_TINRelief, "{" + XMLNamespaces.gml+ "}" + 'name')
      gml_name.text = "ground"
      dem_lod = SubElement(dem_TINRelief, "{" + XMLNamespaces.dem+ "}" + 'lod')
      dem_lod.text = "1"
      dem_tin =  SubElement(dem_TINRelief, "{" + XMLNamespaces.dem+ "}" + 'tin')
      
      gml_TriangulatedSurface = SubElement(dem_tin, "{" + XMLNamespaces.gml+ "}" + 'TriangulatedSurface')
      
      gml_trianglePatches = SubElement(gml_TriangulatedSurface, "{" + XMLNamespaces.gml+ "}" + 'trianglePatches')

      for geometry in geometry_list:
         gml_trianglePatches.append(geometry.construct())
   
   return cityObjectMember
   
   
def write_transportation(trpt_type, lod, name, geometry_list, rd_class = None, function = None, generic_attrib_dict= None):
   cityObjectMember = Element('cityObjectMember')
   tran_trpt_type = SubElement(cityObjectMember, "{" + XMLNamespaces.trans+ "}" + trpt_type)
   tran_trpt_type.attrib["{" + XMLNamespaces.gml+ "}" +'id'] = name

   gml_name = SubElement(tran_trpt_type, "{" + XMLNamespaces.gml+ "}" + 'name')
   gml_name.text = name
   
   #=======================================================================================================
   #attrib
   #=======================================================================================================
   if rd_class !=None:
       tran_class = SubElement(tran_trpt_type,"{" + XMLNamespaces.trans+ "}" + 'class')
       tran_class.text = rd_class
   if function != None:
       tran_function = SubElement(tran_trpt_type,"{" + XMLNamespaces.trans+ "}" + 'function')
       tran_function.text = function
   if generic_attrib_dict != None:
       write_gen_Attribute(tran_trpt_type, generic_attrib_dict)
       
   #=======================================================================================================
   #geometries
   #=======================================================================================================
   if lod == "lod0":
      tran_lod0Network = SubElement(tran_trpt_type, "{" + XMLNamespaces.trans+ "}" + 'lod0Network')
      gml_GeometricComplex = SubElement(tran_lod0Network, "{" + XMLNamespaces.gml+ "}" + 'GeometricComplex')
      
      for geometry in geometry_list:
         gml_element = SubElement(gml_GeometricComplex, "{" + XMLNamespaces.gml+ "}" + 'element')
         gml_element.append(geometry.construct())
         gml_GeometricComplex.append(gml_element)
   
   return cityObjectMember

def write_building(lod, name, geometry_list, bldg_class = None,function = None, usage = None,yr_constr  = None,
                   rooftype = None,height = None,stry_abv_grd = None, stry_blw_grd = None, generic_attrib_dict=None ):
   
   cityObjectMember = Element('cityObjectMember')
   bldg_Building = SubElement(cityObjectMember, "{" + XMLNamespaces.bldg + "}" + "Building")
   bldg_Building.attrib["{" + XMLNamespaces.gml+ "}" +'id'] = name        
   #=======================================================================================================
   #attrib
   #=======================================================================================================
   if bldg_class != None:
       b_class = SubElement(bldg_Building,"{" + XMLNamespaces.bldg+ "}" + 'class')
       b_class.text = bldg_class
       
   if function!=None:
       bldg_function = SubElement(bldg_Building,"{" + XMLNamespaces.bldg+ "}" + 'function')
       bldg_function.text = function
       
   if usage != None:
       bldg_usage = SubElement(bldg_Building,"{" + XMLNamespaces.bldg+ "}" + 'usage')
       bldg_usage.text = usage
       
   if yr_constr != None:
       bldg_yearOfConstruction = SubElement(bldg_Building,"{" + XMLNamespaces.bldg+ "}" + 'yearOfConstruction')
       bldg_yearOfConstruction.text = yr_constr

   if rooftype != None:
       bldg_roofType = SubElement(bldg_Building,"{" + XMLNamespaces.bldg+ "}" + 'roofType')
       bldg_roofType.text = rooftype
   if height!=None:
       bldg_measuredHeight = SubElement(bldg_Building,"{" + XMLNamespaces.bldg+ "}" + 'measuredHeight')
       bldg_measuredHeight.attrib['uom'] = "m"
       bldg_measuredHeight.text = height
       
   if stry_abv_grd != None:
       bldg_storeysAboveGround = SubElement(bldg_Building,"{" + XMLNamespaces.bldg+ "}" + 'storeysAboveGround')
       bldg_storeysAboveGround.text = stry_abv_grd
       
   if stry_blw_grd != None:
       bldg_storeysBelowGround = SubElement(bldg_Building,"{" + XMLNamespaces.bldg+ "}" + 'storeysBelowGround')
       bldg_storeysBelowGround.text = stry_blw_grd
       
   if generic_attrib_dict != None:
       write_gen_Attribute(bldg_Building, generic_attrib_dict)
   
   #=======================================================================================================
   #geometries
   #=======================================================================================================
   if lod == "lod1":
      bldg_lod1Solid = SubElement(bldg_Building, "{" + XMLNamespaces.bldg+ "}" + 'lod1Solid')
      gml_Solid = SubElement(bldg_lod1Solid, "{" + XMLNamespaces.gml+ "}" + 'Solid')
      gml_exterior = SubElement(gml_Solid, "{" + XMLNamespaces.gml+ "}" + 'exterior')
      gml_CompositeSurface = SubElement(gml_exterior, "{" + XMLNamespaces.gml+ "}" + 'CompositeSurface')
      for geometry in geometry_list:
         gml_CompositeSurface.append(geometry.construct())
   
   return cityObjectMember

def write_cityfurniture(lod, name, geometry_list, furn_class = None,function = None, generic_attrib_dict = None ):
   cityObjectMember = Element('cityObjectMember')
   frn_CityFurniture = SubElement(cityObjectMember,"{" + XMLNamespaces.frn+ "}" + 'CityFurniture')
   frn_CityFurniture.attrib["{" + XMLNamespaces.gml+ "}" +'id'] = name
   
   creationDate = SubElement(frn_CityFurniture, 'creationDate')
   creationDate.text = str(datetime.datetime.now())
   
   #=======================================================================================================
   #attrib
   #=======================================================================================================
   if furn_class !=None:
       frn_class = SubElement(frn_CityFurniture,"{" + XMLNamespaces.frn+ "}" + 'class')
       frn_class.text = furn_class
   if function != None:
       frn_function = SubElement(frn_CityFurniture,"{" + XMLNamespaces.frn+ "}" + 'function')
       frn_function.text = function
   if generic_attrib_dict != None:
       write_gen_Attribute(frn_CityFurniture, generic_attrib_dict)
   
   #=======================================================================================================
   #geometries
   #=======================================================================================================
   if lod == "lod1":
      lod1Geometry = SubElement(frn_CityFurniture, "{" + XMLNamespaces.frn+ "}" + 'lod1Geometry')
      gml_Solid = SubElement(lod1Geometry, "{" + XMLNamespaces.gml+ "}" + 'Solid')
      gml_exterior = SubElement(gml_Solid, "{" + XMLNamespaces.gml+ "}" + 'exterior')
      gml_CompositeSurface = SubElement(gml_exterior, "{" + XMLNamespaces.gml+ "}" + 'CompositeSurface')
      for geometry in geometry_list:
         gml_CompositeSurface.append(geometry.construct())

      '''
      #==================================================================
      #reference geometries script TODO: Make it work 
      #==================================================================
      frn_lod1ImplicitRepresentation = SubElement(frn_CityFurniture,"{" + XMLNamespaces.frn+ "}" + 'lod1ImplicitRepresentation')
      ImplicitGeometry = SubElement(frn_lod1ImplicitRepresentation,'ImplicitGeometry')
      mimeType = SubElement(ImplicitGeometry,'mimeType')
      mimeType.text = geometry_type
      libraryObject = SubElement(ImplicitGeometry,'libraryObject')
      libraryObject.text = ref_geometry
      referencePoint = SubElement(ImplicitGeometry,'referencePoint')
      referencePoint.append(ref_pt.construct())
      '''
   
   return cityObjectMember
