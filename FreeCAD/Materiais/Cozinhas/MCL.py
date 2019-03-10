#App.newDocument("MCL_001")
#App.setActiveDocument("MCL_001")
#App.ActiveDocument=App.getDocument("MCL_001")
#Gui.ActiveDocument=Gui.getDocument("MCL_001")

#----------------------------------------- ILHARGA BASE ESQUERDA 700*580*16 ---------------------------------------
App.ActiveDocument.addObject("Part::Box","Box1")
App.ActiveDocument.getObject("Box1").Height = '700 mm'
App.ActiveDocument.getObject("Box1").Width = '16 mm'
App.ActiveDocument.getObject("Box1").Length = '580 mm'
#----------------------------------------- RASGO PARA AS COSTAS 8mm ---------------------------------------
App.ActiveDocument.addObject("Part::Box","Box2")
App.ActiveDocument.getObject("Box2").Height = '700 mm'
App.ActiveDocument.getObject("Box2").Width = '8 mm'
App.ActiveDocument.getObject("Box2").Length = '8 mm'
App.ActiveDocument.getObject("Box2").Placement = App.Placement(App.Vector(71,8,0),App.Rotation(App.Vector(0,0,1),0))
App.activeDocument().addObject("Part::Cut","Cut01")
App.activeDocument().Cut01.Base = App.activeDocument().Box1
App.activeDocument().Cut01.Tool = App.activeDocument().Box2
Gui.activeDocument().hide("Box1")
Gui.activeDocument().hide("Box2")
Gui.ActiveDocument.Cut01.ShapeColor=Gui.ActiveDocument.Box1.ShapeColor
Gui.ActiveDocument.Cut01.DisplayMode=Gui.ActiveDocument.Box1.DisplayMode

#----------------------------------------- FURAÇÃO PARA PARAFUSOS ---------------------------------------
App.ActiveDocument.addObject("Part::Cylinder","Cylinder01")
App.ActiveDocument.getObject("Cylinder01").Radius = '4 mm'
App.ActiveDocument.getObject("Cylinder01").Height = '16 mm'
App.ActiveDocument.getObject("Cylinder01").Placement = App.Placement(App.Vector(100,0,8),App.Rotation(App.Vector(1,0,0),270))
App.activeDocument().addObject("Part::Cut","Cut02")
App.activeDocument().Cut02.Base = App.activeDocument().Cut01
App.activeDocument().Cut02.Tool = App.activeDocument().Cylinder01
Gui.activeDocument().hide("Cut01")
Gui.activeDocument().hide("Cylinder01")
Gui.ActiveDocument.Cut02.ShapeColor=Gui.ActiveDocument.Cut01.ShapeColor
Gui.ActiveDocument.Cut02.DisplayMode=Gui.ActiveDocument.Cut01.DisplayMode

App.ActiveDocument.addObject("Part::Cylinder","Cylinder02")
App.ActiveDocument.getObject("Cylinder02").Radius = '4 mm'
App.ActiveDocument.getObject("Cylinder02").Height = '16 mm'
App.ActiveDocument.getObject("Cylinder02").Placement = App.Placement(App.Vector(300,0,8),App.Rotation(App.Vector(1,0,0),270))
App.activeDocument().addObject("Part::Cut","Cut03")
App.activeDocument().Cut03.Base = App.activeDocument().Cut02
App.activeDocument().Cut03.Tool = App.activeDocument().Cylinder02
Gui.activeDocument().hide("Cut02")
Gui.activeDocument().hide("Cylinder02")
Gui.ActiveDocument.Cut03.ShapeColor=Gui.ActiveDocument.Cut02.ShapeColor
Gui.ActiveDocument.Cut03.DisplayMode=Gui.ActiveDocument.Cut02.DisplayMode

App.ActiveDocument.addObject("Part::Cylinder","Cylinder03")
App.ActiveDocument.getObject("Cylinder03").Radius = '4 mm'
App.ActiveDocument.getObject("Cylinder03").Height = '16 mm'
App.ActiveDocument.getObject("Cylinder03").Placement = App.Placement(App.Vector(520,0,8),App.Rotation(App.Vector(1,0,0),270))
App.activeDocument().addObject("Part::Cut","Cut04")
App.activeDocument().Cut04.Base = App.activeDocument().Cut03
App.activeDocument().Cut04.Tool = App.activeDocument().Cylinder03
Gui.activeDocument().hide("Cut03")
Gui.activeDocument().hide("Cylinder03")
Gui.ActiveDocument.Cut04.ShapeColor=Gui.ActiveDocument.Cut03.ShapeColor
Gui.ActiveDocument.Cut04.DisplayMode=Gui.ActiveDocument.Cut03.DisplayMode

App.ActiveDocument.addObject("Part::Cylinder","Cylinder04")
App.ActiveDocument.getObject("Cylinder04").Radius = '4 mm'
App.ActiveDocument.getObject("Cylinder04").Height = '16 mm'
App.ActiveDocument.getObject("Cylinder04").Placement = App.Placement(App.Vector(100,0,692),App.Rotation(App.Vector(1,0,0),270))
App.activeDocument().addObject("Part::Cut","Cut05")
App.activeDocument().Cut05.Base = App.activeDocument().Cut04
App.activeDocument().Cut05.Tool = App.activeDocument().Cylinder04
Gui.activeDocument().hide("Cut04")
Gui.activeDocument().hide("Cylinder04")
Gui.ActiveDocument.Cut05.ShapeColor=Gui.ActiveDocument.Cut04.ShapeColor
Gui.ActiveDocument.Cut05.DisplayMode=Gui.ActiveDocument.Cut04.DisplayMode

App.ActiveDocument.addObject("Part::Cylinder","Cylinder05")
App.ActiveDocument.getObject("Cylinder05").Radius = '4 mm'
App.ActiveDocument.getObject("Cylinder05").Height = '16 mm'
App.ActiveDocument.getObject("Cylinder05").Placement = App.Placement(App.Vector(300,0,692),App.Rotation(App.Vector(1,0,0),270))
App.activeDocument().addObject("Part::Cut","Cut06")
App.activeDocument().Cut06.Base = App.activeDocument().Cut05
App.activeDocument().Cut06.Tool = App.activeDocument().Cylinder05
Gui.activeDocument().hide("Cut05")
Gui.activeDocument().hide("Cylinder05")
Gui.ActiveDocument.Cut06.ShapeColor=Gui.ActiveDocument.Cut05.ShapeColor
Gui.ActiveDocument.Cut06.DisplayMode=Gui.ActiveDocument.Cut05.DisplayMode

App.ActiveDocument.addObject("Part::Cylinder","Cylinder06")
App.ActiveDocument.getObject("Cylinder06").Radius = '4 mm'
App.ActiveDocument.getObject("Cylinder06").Height = '16 mm'
App.ActiveDocument.getObject("Cylinder06").Placement = App.Placement(App.Vector(520,0,692),App.Rotation(App.Vector(1,0,0),270))
App.activeDocument().addObject("Part::Cut","Cut07")
App.activeDocument().Cut07.Base = App.activeDocument().Cut06
App.activeDocument().Cut07.Tool = App.activeDocument().Cylinder06
Gui.activeDocument().hide("Cut06")
Gui.activeDocument().hide("Cylinder06")
Gui.ActiveDocument.Cut07.ShapeColor=Gui.ActiveDocument.Cut06.ShapeColor
Gui.ActiveDocument.Cut07.DisplayMode=Gui.ActiveDocument.Cut06.DisplayMode

#----------------------------------------- FURAÇÃO PARA CAVILHAS ---------------------------------------
App.ActiveDocument.addObject("Part::Cylinder","Cylinder08")
App.ActiveDocument.getObject("Cylinder08").Radius = '4 mm'
App.ActiveDocument.getObject("Cylinder08").Height = '8 mm'
App.ActiveDocument.getObject("Cylinder08").Placement = App.Placement(App.Vector(165,8,8),App.Rotation(App.Vector(1,0,0),270))

App.ActiveDocument.addObject("Part::Cylinder","Cylinder09")
App.ActiveDocument.getObject("Cylinder09").Radius = '4 mm'
App.ActiveDocument.getObject("Cylinder09").Height = '8 mm'
App.ActiveDocument.getObject("Cylinder09").Placement = App.Placement(App.Vector(260,8,8),App.Rotation(App.Vector(1,0,0),270))
App.ActiveDocument.addObject("Part::Cylinder","Cylinder10")
App.ActiveDocument.getObject("Cylinder10").Radius = '4 mm'
App.ActiveDocument.getObject("Cylinder10").Height = '8 mm'
App.ActiveDocument.getObject("Cylinder10").Placement = App.Placement(App.Vector(355,8,8),App.Rotation(App.Vector(1,0,0),270))
App.ActiveDocument.addObject("Part::Cylinder","Cylinder11")
App.ActiveDocument.getObject("Cylinder11").Radius = '4 mm'
App.ActiveDocument.getObject("Cylinder11").Height = '8 mm'
App.ActiveDocument.getObject("Cylinder11").Placement = App.Placement(App.Vector(450,8,8),App.Rotation(App.Vector(1,0,0),270))
App.ActiveDocument.addObject("Part::Cylinder","Cylinder12")
App.ActiveDocument.getObject("Cylinder12").Radius = '4 mm'
App.ActiveDocument.getObject("Cylinder12").Height = '8 mm'
App.ActiveDocument.getObject("Cylinder12").Placement = App.Placement(App.Vector(545,8,8),App.Rotation(App.Vector(1,0,0),270))


#----------------------------------------- FURAÇÃO PARA PRATELEIRAS ---------------------------------------
App.ActiveDocument.recompute()

Gui.activeDocument().activeView().viewAxonometric()
Gui.SendMsgToActiveView("ViewFit")





