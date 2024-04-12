bl_info = {
    "name": "LEGO Realisticifier",
    "author": "KKS (-人-) ",
    "version": (1, 0),
    "blender": (2, 80, 0),
    "location": "View3D > Add > Mesh > New Object",
    "description": "Shortcut tool for Highly Detailed LEGO Realistic renders.",
    "warning": "This may slow your PC",
    "doc_url": "",
    "category": "",
}


import bpy
import os
from random import randint
from bpy.types import (Panel, Operator)

inner_path = 'Collection'
collection_name = 'Dust/Hair Assets'
collection_name2 = 'Dusty Air'

class ButtonOperator(bpy.types.Operator):
    """Import Dust"""
    bl_idname = "random.1"
    bl_label = "Simple Random Operator"

    def execute(self, context):
        
        for obj in bpy.context.selected_objects:
            bpy.ops.wm.append(
                directory=os.path.join(os.path.dirname(__file__), 'assets', 'Dust_Hair_Asset.blend', inner_path, collection_name)
                )
        ##Remove Unnecessary Collections
            if "Dust/Hair Assets.001" in bpy.data.collections:
                    removecollections = bpy.data.collections["Dust/Hair Assets.001"]
                    print("removing collection", removecollections)
                    bpy.data.collections.remove(removecollections)
                
            Dust = bpy.data.collections["Dust/Hair Assets"]
            
            if len(obj.particle_systems) == 0:
                
                obj.modifiers.new("Dust importer",type='PARTICLE_SYSTEM')
                part = obj.particle_systems[0]
                
                settings = obj.particle_systems[0].settings                    
                settings.type = 'HAIR'
                settings.use_advanced_hair = True
                settings.use_rotations = True
                settings.rotation_factor_random = 1
                settings.phase_factor = 1
                settings.phase_factor_random = 2
                settings.instance_collection = Dust
                settings.count = 460
                settings.render_type = 'COLLECTION'
                settings.distribution = 'RAND'
                settings.particle_size = 0.35
        return {'FINISHED'}
    
class ButtonOperatorDustyAir(bpy.types.Operator):
    """Import Dusty Air"""
    bl_idname = "random.5"
    bl_label = "OperatorDustyAir"

    def execute(self, context):
        bpy.ops.wm.append(
            directory=os.path.join(os.path.dirname(__file__), 'assets', 'Dusty_Air.blend', inner_path, collection_name2)
            )
            
        return {'FINISHED'}

class ButtonOperator3(bpy.types.Operator):
    """Hide on Viewport"""
    bl_idname = "random.3"
    bl_label = "Simple Random Operator3"

    def execute(self, context):
        ##Hide in Viewport
        bpy.context.object.modifiers["ParticleSystem"].show_viewport = False
        print("Hided on Viewport")
        
        return {'FINISHED'}

class ButtonOperatorHideAirDust(bpy.types.Operator):
    """Hide on Viewport"""
    bl_idname = "random.6"
    bl_label = "OperatorHideDust"

    def execute(self, context):
        ##Hide in Viewport
        bpy.context.object.modifiers["DustInTheAirParticle"].show_viewport = False
        print("Hided on Viewport")
        
        return {'FINISHED'}



class ButtonOperator4(bpy.types.Operator):
    """Hide on Viewport"""
    bl_idname = "random.4"
    bl_label = "Simple Random Operator4"

    def execute(self, context):
        ##Weight Paint
        bpy.ops.object.vertex_group_add()
        bpy.ops.paint.weight_paint_toggle()
        bpy.ops.object.vertex_group_invert(group_select_mode='ACTIVE', auto_assign=True)
        bpy.context.object.particle_systems["Dust importer"].vertex_group_density = "Group"
        print("Weight Paint Activated")
        
        return {'FINISHED'}

class AddonPanel(bpy.types.Panel):
    bl_label = "LEGO Realisticifier"
    bl_idname = "OBJECT_PT_random"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "LEGO Realisticifier"

    def draw(self, context):
        layout = self.layout
        obj = context.object
        row = layout.row()
        row.label(text = r"""𝗗𝘂𝘀𝘁 𝗜𝗺𝗽𝗼𝗿𝘁𝗲𝗿""", icon='OUTLINER_DATA_POINTCLOUD')
        
        row = layout.row()
        row.scale_y = 1
        row.operator(ButtonOperator.bl_idname, text="Import Dust", icon='IMPORT')
        
        
        row.scale_y = 1.5
        row = layout.row()
        row.scale_y = 1
        row.label(text = r"""𝙩𝙝𝙞𝙨 𝙢𝙖𝙮 𝙨𝙡𝙤𝙬 𝙙𝙤𝙬𝙣 𝙮𝙤𝙪𝙧 𝙘𝙤𝙢𝙥𝙪𝙩𝙚𝙧""", icon='ERROR')

class AddonPanel2(bpy.types.Panel):
    bl_label = "Dust Settings"
    bl_idname = "PT_DustSettings"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "LEGO Realisticifier"
    
    def draw(self, context):
        layout = self.layout
        obj = context.object
        
        row = layout.row()
        layout.separator(factor=0.3)
        row.label(text = r"""𝗗𝘂𝘀𝘁 𝗦𝗲𝘁𝘁𝗶𝗻𝗴𝘀""", icon='OUTLINER_DATA_POINTCLOUD')
        
        row = layout.row()
        row.label(text = "Scale", icon='CURVE_NCIRCLE')
        
        row.prop(bpy.data.particles['ParticleSettings'], 'particle_size', text='', icon_value=0, emboss=True)
        
        row = layout.row()
        row.label(text = "Scale Randomness", icon='SURFACE_NCIRCLE')
        
        row.prop(bpy.data.particles['ParticleSettings'], 'size_random', text='', icon_value=0, emboss=True)
        
        row = layout.row()
        row.label(text = "Amount", icon='LINENUMBERS_ON')
        
        row.prop(bpy.data.particles['ParticleSettings'], 'count', text='', icon_value=0, emboss=True)
        
        row = layout.row()
        row.label(text = "Seed", icon='CURVES_DATA')
        row.prop(bpy.context.object.particle_systems["Dust importer"], 'seed', text='', icon_value=0, emboss=True)
        
        row = layout.row()
        layout.separator(factor=0.3)
        row.label(text = r"""𝗠𝗮𝘁𝗲𝗿𝗶𝗮𝗹 𝗦𝗲𝘁𝘁𝗶𝗻𝗴𝘀""", icon='MATERIAL')
        
        row = layout.row()
        row.label(text = "Dust Color", icon='COLOR')
        row.prop(bpy.data.materials["Dust Material"].node_tree.nodes["Transparent BSDF"].inputs[0], 'default_value', text='', icon_value=0, emboss=True)
        
        row = layout.row()
        row.label(text = "Transparency", icon='TEXTURE_DATA')
        row.prop(bpy.data.materials["Dust Material"].node_tree.nodes["Mix Shader"].inputs[0], 'default_value', text='Transparency', icon_value=0, emboss=True)
        
        row = layout.row()
        row.label(text = "Roughness", icon='VPAINT_HLT')
        row.prop(bpy.data.materials["Dust Material"].node_tree.nodes["Diffuse BSDF"].inputs[1], 'default_value', text='Roughness', icon_value=0, emboss=True)
        
        row = layout.row()
        row.label(text = "Detail", icon='OUTLINER_DATA_LIGHTPROBE')
        row.prop(bpy.data.materials["Dust Material"].node_tree.nodes["Voronoi Texture"].inputs[2], 'default_value', text='Detail', icon_value=0, emboss=True)
        
        row = layout.row()
        layout.separator(factor=0.1)
        row.label(text = r"""𝘯𝘰𝘵𝘦: 𝘺𝘰𝘶 𝘤𝘢𝘯 𝘤𝘶𝘴𝘵𝘰𝘮𝘪𝘻𝘦 𝘮𝘰𝘳𝘦 𝘴𝘦𝘵𝘵𝘪𝘯𝘨𝘴 𝘪𝘯 "𝘋𝘶𝘴𝘵 𝘔𝘢𝘵𝘦𝘳𝘪𝘢𝘭".""", icon='COPYDOWN')
        
        row = layout.row()
        layout.separator(factor=0.3)
        row.label(text = r"""𝗘𝘅𝘁𝗿𝗮""", icon='COLLAPSEMENU')
        
        row = layout.row()
        row.prop(bpy.data.particles["ParticleSettings"], "use_parent_particles", text='Use Parent Particles', icon_value=0, emboss=True)
        
        row = layout.row()
        row.label(text = "Weight Paint Control (E̲xperimental)", icon='WPAINT_HLT')
        row.operator(ButtonOperator4.bl_idname, text="Control", icon='GREASEPENCIL')
        
        row = layout.row()
        row.label(text = """𝘠𝘰𝘶 𝘯𝘦𝘦𝘥 𝘵𝘰 𝘪𝘯𝘷𝘦𝘳𝘵 𝘵𝘩𝘦 𝘷𝘦𝘳𝘵𝘦𝘹 𝘨𝘳𝘰𝘶𝘱. "𝘞𝘦𝘪𝘨𝘩𝘵𝘴" > "𝘐𝘯𝘷𝘦𝘳𝘵" """, icon='ERROR')
        
        layout.separator(factor=0.15)
        
        row = layout.row()
        row.label(text = "Viewport Amount", icon='LOCKVIEW_ON')
        row.prop(bpy.data.particles["ParticleSettings"], "display_percentage", text='', icon_value=0, emboss=True)
        
        
        row = layout.row()
        row.scale_y = 1.2
        row.operator(ButtonOperator3.bl_idname, text="Hide on Viewport", icon='RESTRICT_VIEW_ON')


class AddonPanel3(bpy.types.Panel):
    bl_label = "Air Dustifier"
    bl_idname = "PT_DustToAir"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "LEGO Realisticifier"
    
    def draw(self, context):
        layout = self.layout
        obj = context.object
        
        row = layout.row()
        row.label(text = r"""𝗜𝗺𝗽𝗼𝗿𝘁 𝗗𝘂𝘀𝘁𝘆 𝗔𝗶𝗿""", icon='OUTLINER_DATA_POINTCLOUD')
        
        row = layout.row()
        row.scale_y = 1.5
        row.operator(ButtonOperatorDustyAir.bl_idname, text="Import Dusty Air", icon='IMPORT')
        
        row.scale_y = 1.5
        row = layout.row()
        row.scale_y = 1
        row.label(text = r"""𝘜𝘴𝘦 𝘋𝘰𝘍 𝘰𝘳 𝘉𝘰𝘬𝘦𝘩 - 𝘉𝘦𝘴𝘵 𝘙𝘦𝘴𝘶𝘭𝘵""", icon='ERROR')
        
        row = layout.row()
        layout.separator(factor=0.3)
        row.label(text = r"""𝗦𝗲𝘁𝘁𝗶𝗻𝗴𝘀""", icon='SETTINGS')
        
        row = layout.row()
        row.label(text = "Emission Color", icon='LIGHT_SUN')
        row.prop(bpy.data.materials["DustInAirDustMaterial"].node_tree.nodes["Principled BSDF"].inputs[26], "default_value", text='', icon_value=0, emboss=True)
        
        row = layout.row()
        row.label(text = "Scale", icon='CURVE_NCIRCLE')
        row.prop(bpy.data.particles['DustInTheAirParticle'], 'particle_size', text='', icon_value=0, emboss=True)
        
        row = layout.row()
        row.label(text = "Amount", icon='LINENUMBERS_ON')
        row.prop(bpy.data.particles['DustInTheAirParticle'], 'count', text='', icon_value=0, emboss=True)
        
        row = layout.row()
        row.label(text = "Seed", icon='CURVES_DATA')
        row.prop(bpy.context.object.particle_systems["DustInTheAirParticle"], 'seed', text='', icon_value=0, emboss=True)
        
        row = layout.row()
        row.scale_y = 1.2
        row.operator(ButtonOperatorHideAirDust.bl_idname, text="Hide on Viewport", icon='RESTRICT_VIEW_ON')
        
        
        
        
from bpy.utils import register_class, unregister_class

_classes = [
    ButtonOperator,
    ButtonOperator2,
    ButtonOperator3,
    ButtonOperator4,
    ButtonOperatorDustyAir,
    ButtonOperatorHideAirDust,
    AddonPanel,
    AddonPanel2,
    AddonPanel3
]



def register():
    from bpy.utils import register_class
    for cls in _classes:
        register_class(cls)
    
def unregister():
    from bpy.utils import unregister_class
    for cls in _classes:
        unregister_class(cls)
    
    
if __name__ == "__main__":
    register()
