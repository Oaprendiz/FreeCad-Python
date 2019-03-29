# http://miba.juergen-riegel.net/
# https://www.freecadweb.org/wiki/MIBA
# https://www.freecadweb.org/wiki/index.php?title=Std_ViewScreenShot
# https://forum.freecadweb.org/viewtopic.php?t=18340
# https://www.youtube.com/watch?v=uPoTIBMXr8w
# https://www.youtube.com/watch?v=2zfzZC-TnmU
# http://willms.pagesperso-orange.fr/freecad/freecad_tweak.html
#
# https://www.youtube.com/watch?v=khOfh303JZQ
# https://www.youtube.com/watch?v=m94HQP1pC0U
# https://www.youtube.com/watch?v=sOtgKQTBfYo
# https://www.youtube.com/watch?v=G6CUp15DdU4
# https://www.youtube.com/watch?v=gXB6D2yOY80
# https://www.youtube.com/watch?v=7XcmiZ2s0uI
# https://www.youtube.com/watch?v=VUlUMWje_qw
# https://www.youtube.com/watch?v=kkvU3dvMkSI
# https://www.youtube.com/watch?v=gQvFctA1HNI
# https://www.youtube.com/watch?v=z3gZEncypG8
# 


#exec(open('Z:\GitHub\FreeCad-Python\FreeCAD\Materiais\Cozinhas\MCL001.py').read())

import os

def exportViewToPNG():
    '''Exports the current view to a PNG suitable for printing on A4 or Letter.
       The filename will be e.g. MyProject-view.png in the project directory.'''
    # Reference: http://www.freecadweb.org/wiki/index.php?title=Std_ViewScreenShot

    # Create an image which fits on an A4 or Letter page at 300dpi, landscape
    width = 11 * 300    # inside letter
    height = int(8.26 * 300) # inside A4

    doc = FreeCAD.ActiveDocument

    if not doc.FileName:
        FreeCAD.Console.PrintError('Must save project first\n')
        return

    docDir, docFilename = os.path.split(doc.FileName)

    filePrefix = os.path.splitext(docFilename)[0]

    filename = filePrefix + '-view.png'
    filePath = os.path.join(docDir, filename)

    FreeCAD.Console.PrintMessage("Saving view to %s\n" % filePath)
    FreeCADGui.ActiveDocument.ActiveView.saveImage(filePath.encode("utf-8"), width, height, 'White')

def kit0000(nAlt, nLarg, nEsp = nAgl): # Peça c/medidas livres (elemento básico)
	global nKit, cKit
	nKit += 1
	cKit = "Kit" + str(nKit).zfill(5)
	App.ActiveDocument.addObject("Part::Box", cKit)
	App.ActiveDocument.getObject(cKit).Height = str(nAlt) + ' mm'
	App.ActiveDocument.getObject(cKit).Width = str(nLarg) + ' mm'
	App.ActiveDocument.getObject(cKit).Length = str(nEsp) + ' mm'

def kit0001(nAlt, nLarg, nPos = 1, nEsp = nAgl): # Ilharga Base c/rasgo e furação para dobradiças
#	global nKit, cKit, nDis_dob
	kit0000(nAlt, nLarg, nEsp)
	kit0050(nAlt, nLarg - 59, nPos) # rasgo vertical
	kit0051(nAlt, nPos)             # furos para dobradiças

def kit0002(nAlt, nLarg, nPos = 1, nEsp = nAgl): # Ilharga Base c/rasgo, furação para dobradiças e prateleiras
	global nKit, cKit
	kit0001(nAlt, nLarg, nPos, nEsp)             # Ilharga Base
	kit0053(4, nDis_prat, nMB_alto, nPos)        # Dobradiças
	kit0053(4, nDis_prat + 380, nMB_alto, nPos)  # Prateleiras

def kit0003(nLarg, nFundo, nPos = 1, nEsp = nAgl): # Topo e Base p/MB
	global nKit, nKit
	kit0000(nEsp, nFundo, nLarg)
	if nPos == 1:
		kit0050(nLarg, nFundo - 24, 3) # 1 = rasgo horizontal topo
	else:
		kit0050(nLarg, nFundo - 24, 4) # 2 = rasgo horizontal base

def kit0004(nAlt, nLarg, nPos = 1, nEsp = nAgl): # Ilharga Base s/rasgo e c/furação para dobradiças
	global nKit, cKit
	kit0000(nAlt, nLarg, nEsp)
	kit0051(nAlt, nPos)             # furos para dobradiças

def kit0005(nAlt, nLarg, nEsp = 8): # Costa Base
	kit0000(nAlt, nEsp, nLarg)

def kit0006(nLarg, nFundo, nEsp = nAgl): # Prateleira Base
	kit0000(nEsp, nFundo, nLarg)



# ---------------------------------------------------------------------------------------------------


def kit0050(nDim, nDis, nPos = 1): # Rasgo para as costas ou fundo de gavetas
	if nPos in range(1, 5):
		global nKit, cKit, nRas_alto, nRas_largo
		cBase = "Kit" + str(nKit).zfill(5)
		nKit += 1
		cKit = "Kit" + str(nKit).zfill(5)
		App.ActiveDocument.addObject("Part::Box", cKit)
		if nPos == 1 or nPos == 2: # vertical trás esq/dir
			App.ActiveDocument.getObject(cKit).Height = str(nDim) + ' mm'
			App.ActiveDocument.getObject(cKit).Width = str(nRas_alto) + ' mm'
			App.ActiveDocument.getObject(cKit).Length = str(nRas_largo) + ' mm'
			if nPos == 1:
				App.ActiveDocument.getObject(cKit).Placement = App.Placement(App.Vector(0, nDis, nRas_alto),App.Rotation(App.Vector(0, 0, 1),0))
			else:
				App.ActiveDocument.getObject(cKit).Placement = App.Placement(App.Vector(0, nDis, 0),App.Rotation(App.Vector(0,0,1),0))
		elif nPos == 3 or nPos ==4:
			App.ActiveDocument.getObject(cKit).Height = str(nRas_largo) + ' mm'
			App.ActiveDocument.getObject(cKit).Width = str(nRas_alto) + ' mm'
			App.ActiveDocument.getObject(cKit).Length = str(nDim) + ' mm'
			if nPos == 3:
				App.ActiveDocument.getObject(cKit).Placement = App.Placement(App.Vector(0, nDis, 0),App.Rotation(App.Vector(0, 0, 1),0))
			else:
				App.ActiveDocument.getObject(cKit).Placement = App.Placement(App.Vector(0, nDis, nRas_alto),App.Rotation(App.Vector(0,0,1),0))
		elif nPos == 5 or nPos ==6:
			print ("horizontal topos e fundos")
		cTool = cKit
		nKit +=1
		cKit = "Kit" + str(nKit).zfill(5)
		App.activeDocument().addObject("Part::Cut", cKit)
		App.activeDocument().getObject(cKit).Base = App.activeDocument().getObject(cBase)
		App.activeDocument().getObject(cKit).Tool = App.activeDocument().getObject(cTool)
		Gui.activeDocument().hide(cBase)
		Gui.activeDocument().hide(cTool)
		Gui.ActiveDocument.getObject(cKit).ShapeColor=Gui.ActiveDocument.getObject(cBase).ShapeColor
		Gui.ActiveDocument.getObject(cKit).DisplayMode=Gui.ActiveDocument.getObject(cBase).DisplayMode

def kit0051(nAlt, nPos): # Furo para dobradiças
	global nKit, cKit, nDis_dob, nDis_Fdob, nDis_Adob
	if nPos in range(1, 3):
		nDob = nDis_Adob
		for n in range(2):
			cBase = "Kit" + str(nKit).zfill(5)
			nKit += 1
			cKit = "Kit" + str(nKit).zfill(5)
			App.ActiveDocument.addObject("Part::Cylinder", cKit)
			App.ActiveDocument.getObject(cKit).Radius = '2,5 mm'
			App.ActiveDocument.getObject(cKit).Height = '8 mm'
			if nPos == 1:
				App.ActiveDocument.getObject(cKit).Placement = App.Placement(App.Vector(8, nDis_dob, nDob),App.Rotation(App.Vector(0, 1, 0),90))
			else:
				App.ActiveDocument.getObject(cKit).Placement = App.Placement(App.Vector(0, nDis_dob, nDob),App.Rotation(App.Vector(0,1,),90))
			nDob += nDis_Fdob
			cTool = cKit
			nKit +=1
			cKit = "Kit" + str(nKit).zfill(5)
			App.activeDocument().addObject("Part::Cut", cKit)
			App.activeDocument().getObject(cKit).Base = App.activeDocument().getObject(cBase)
			App.activeDocument().getObject(cKit).Tool = App.activeDocument().getObject(cTool)
			Gui.activeDocument().hide(cBase)
			Gui.activeDocument().hide(cTool)
			Gui.ActiveDocument.getObject(cKit).ShapeColor=Gui.ActiveDocument.getObject(cBase).ShapeColor
			Gui.ActiveDocument.getObject(cKit).DisplayMode=Gui.ActiveDocument.getObject(cBase).DisplayMode
		nDob = nAlt - nDis_Adob
		for n in range(2):
			cBase = "Kit" + str(nKit).zfill(5)
			nKit += 1
			cKit = "Kit" + str(nKit).zfill(5)
			App.ActiveDocument.addObject("Part::Cylinder", cKit)
			App.ActiveDocument.getObject(cKit).Radius = '2,5 mm'
			App.ActiveDocument.getObject(cKit).Height = '8 mm'
			if nPos == 1:
				App.ActiveDocument.getObject(cKit).Placement = App.Placement(App.Vector(8, nDis_dob, nDob),App.Rotation(App.Vector(0, 1, 0),90))
			else:
				App.ActiveDocument.getObject(cKit).Placement = App.Placement(App.Vector(0, nDis_dob, nDob),App.Rotation(App.Vector(0,1,),90))
			nDob -= nDis_Fdob
			cTool = cKit
			nKit +=1
			cKit = "Kit" + str(nKit).zfill(5)
			App.activeDocument().addObject("Part::Cut", cKit)
			App.activeDocument().getObject(cKit).Base = App.activeDocument().getObject(cBase)
			App.activeDocument().getObject(cKit).Tool = App.activeDocument().getObject(cTool)
			Gui.activeDocument().hide(cBase)
			Gui.activeDocument().hide(cTool)
			Gui.ActiveDocument.getObject(cKit).ShapeColor=Gui.ActiveDocument.getObject(cBase).ShapeColor
			Gui.ActiveDocument.getObject(cKit).DisplayMode=Gui.ActiveDocument.getObject(cBase).DisplayMode

def kit0052(nAlt, nPos): # Furo para optimização
	global nCylinder, nKit
	cFuro = "Cylinder" + str(nCylinder).zfill(5)
	nCylinder += 1
	App.ActiveDocument.addObject("Part::Cylinder",cFuro)
	App.ActiveDocument.getObject(cFuro).Radius = '2,5 mm'
	App.ActiveDocument.getObject(cFuro).Height = '8 mm'
	App.ActiveDocument.getObject(cFuro).Placement = App.Placement(App.Vector(x, z, y),App.Rotation(App.Vector(0,1,0),90))

#	cBase = "Kit" + str(nKit).zfill(5)
#	nKit +=1
#	cKit = "Kit" + str(nKit).zfill(5)
#	App.activeDocument().addObject("Part::Cut", cKit)
#	App.activeDocument().getObject(cKit).Base = App.activeDocument().getObject(cBase)
#	App.activeDocument().getObject(cKit).Tool = App.activeDocument().getObject(cFuro)
#	Gui.activeDocument().hide(cBase)
#	Gui.activeDocument().hide(cFuro)
#	Gui.ActiveDocument.getObject(cKit).ShapeColor=Gui.ActiveDocument.getObject(cBase).ShapeColor
#	Gui.ActiveDocument.getObject(cKit).DisplayMode=Gui.ActiveDocument.getObject(cBase).DisplayMode

def kit0053(nQuant, nDis = nDis_prat, nAlt = nMB_alto, nPos = 1): # Furo para prateleiras
	global nKit, cKit, nDis_Fdob, nDis_Aprat
	if nPos in range(1, 3):
		nPrat = nDis_Aprat
		for n in range(nQuant + 1):
			cBase = "Kit" + str(nKit).zfill(5)
			nKit += 1
			cKit = "Kit" + str(nKit).zfill(5)
			App.ActiveDocument.addObject("Part::Cylinder", cKit)
			App.ActiveDocument.getObject(cKit).Radius = '2,5 mm'
			App.ActiveDocument.getObject(cKit).Height = '8 mm'
			if nPos == 1:
				App.ActiveDocument.getObject(cKit).Placement = App.Placement(App.Vector(8, nDis, nPrat),App.Rotation(App.Vector(0, 1, 0),90))
			else:
				App.ActiveDocument.getObject(cKit).Placement = App.Placement(App.Vector(0, nDis, nPrat),App.Rotation(App.Vector(0,1,),90))
			nPrat += ndis_Fprat
			cTool = cKit
			nKit +=1
			cKit = "Kit" + str(nKit).zfill(5)
			App.activeDocument().addObject("Part::Cut", cKit)
			App.activeDocument().getObject(cKit).Base = App.activeDocument().getObject(cBase)
			App.activeDocument().getObject(cKit).Tool = App.activeDocument().getObject(cTool)
			Gui.activeDocument().hide(cBase)
			Gui.activeDocument().hide(cTool)
			Gui.ActiveDocument.getObject(cKit).ShapeColor=Gui.ActiveDocument.getObject(cBase).ShapeColor
			Gui.ActiveDocument.getObject(cKit).DisplayMode=Gui.ActiveDocument.getObject(cBase).DisplayMode


def kit0099(nLarg): # Movel Base s/Topo (modelo pada MB's forno e LL
	global nKit
	kit0001(700, 580)	# ------------------------------------------------ Ilharga esq.
	cBase = "Kit" + str(nKit).zfill(5)
	App.ActiveDocument.recompute()
	Gui.activeDocument().activeView().viewAxonometric()
	Gui.SendMsgToActiveView("ViewFit")
	kit0005(545, nLarg - 32)	# ------------------------------------------------ Base
	cTool = "Kit" + str(nKit).zfill(5)
	App.ActiveDocument.getObject(cTool).Placement = App.Placement(App.Vector(35, 16, 0),App.Rotation(App.Vector(0,0,1),0))
	nKit += 1
	cFuse = "Kit" + str(nKit).zfill(5)
	App.activeDocument().addObject("Part::Fuse",cFuse)
	App.activeDocument().getObject(cFuse).Base = App.activeDocument().getObject(cBase)
	App.activeDocument().getObject(cFuse).Tool = App.activeDocument().getObject(cTool)
	Gui.activeDocument().hide(cBase)
	Gui.activeDocument().hide(cTool)
	Gui.ActiveDocument.getObject(cFuse).ShapeColor=Gui.ActiveDocument.getObject(cBase).ShapeColor
	Gui.ActiveDocument.getObject(cFuse).DisplayMode=Gui.ActiveDocument.getObject(cBase).DisplayMode
	App.ActiveDocument.recompute()
	Gui.activeDocument().activeView().viewAxonometric()
	Gui.SendMsgToActiveView("ViewFit")
	kit0050(700, 580)	# ------------------------------------------------ Ilharga dir.
	cBase = "Kit" + str(nKit).zfill(5)
	cTool = "Kit" + str(nKit).zfill(5)
	App.ActiveDocument.getObject(cTool).Placement = App.Placement(App.Vector(0, nLarg - 16, 0),App.Rotation(App.Vector(0,0,1),0))
	nKit += 1
	cFuse = "Kit" + str(nKit).zfill(5)
	App.activeDocument().addObject("Part::Fuse",cFuse)
	App.activeDocument().getObject(cFuse).Base = App.activeDocument().getObject(cBase)
	App.activeDocument().getObject(cFuse).Tool = App.activeDocument().getObject(cTool)
	Gui.activeDocument().hide(cBase)
	Gui.activeDocument().hide(cTool)
	Gui.ActiveDocument.getObject(cFuse).ShapeColor=Gui.ActiveDocument.getObject(cBase).ShapeColor
	Gui.ActiveDocument.getObject(cFuse).DisplayMode=Gui.ActiveDocument.getObject(cBase).DisplayMode
	App.ActiveDocument.recompute()
	Gui.activeDocument().activeView().viewAxonometric()
	Gui.SendMsgToActiveView("ViewFit")

def kit0100(nLarg): # Movel Base s/prateleira (modelo para todos os MB's
	global nKit, cKit
	kit0002(700, 580)	# ------------------------------------------------ Ilharga esq.
	cBase = "Kit" + str(nKit).zfill(5)
	kit0007(684, nLarg - 16)	# ---------------------------------------- Costas
	cTool = "Kit" + str(nKit).zfill(5)
	App.ActiveDocument.getObject(cTool).Placement = App.Placement(App.Vector(51,8,8),App.Rotation(App.Vector(0,0,1),0))
	nKit += 1
	cFuse = "Kit" + str(nKit).zfill(5)
	App.activeDocument().addObject("Part::Fuse",cFuse)
	App.activeDocument().getObject(cFuse).Base = App.activeDocument().getObject(cBase)
	App.activeDocument().getObject(cFuse).Tool = App.activeDocument().getObject(cTool)
	Gui.activeDocument().hide(cBase)
	Gui.activeDocument().hide(cTool)
	Gui.ActiveDocument.getObject(cFuse).ShapeColor=Gui.ActiveDocument.getObject(cBase).ShapeColor
	Gui.ActiveDocument.getObject(cFuse).DisplayMode=Gui.ActiveDocument.getObject(cBase).DisplayMode
	App.ActiveDocument.recompute()
	Gui.activeDocument().activeView().viewAxonometric()
	Gui.SendMsgToActiveView("ViewFit")
	kit0050(700, 580)	# ------------------------------------------------ Ilharga dir.
	cBase = "Kit" + str(nKit).zfill(5)
	cTool = "Kit" + str(nKit).zfill(5)
	App.ActiveDocument.getObject(cTool).Placement = App.Placement(App.Vector(0, nLarg - 16, 0),App.Rotation(App.Vector(0,0,1),0))
	nKit += 1
	cFuse = "Kit" + str(nKit).zfill(5)
	App.activeDocument().addObject("Part::Fuse",cFuse)
	App.activeDocument().getObject(cFuse).Base = App.activeDocument().getObject(cBase)
	App.activeDocument().getObject(cFuse).Tool = App.activeDocument().getObject(cTool)
	Gui.activeDocument().hide(cBase)
	Gui.activeDocument().hide(cTool)
	Gui.ActiveDocument.getObject(cFuse).ShapeColor=Gui.ActiveDocument.getObject(cBase).ShapeColor
	Gui.ActiveDocument.getObject(cFuse).DisplayMode=Gui.ActiveDocument.getObject(cBase).DisplayMode
	App.ActiveDocument.recompute()
	Gui.activeDocument().activeView().viewAxonometric()
	Gui.SendMsgToActiveView("ViewFit")
	kit0005(545, nLarg - 32)	# ------------------------------------------------ Base
	cBase = "Kit" + str(nKit).zfill(5)
	cTool = "Kit" + str(nKit).zfill(5)
	App.ActiveDocument.getObject(cTool).Placement = App.Placement(App.Vector(35, 16, 0),App.Rotation(App.Vector(0,0,1),0))
	nKit += 1
	cFuse = "Kit" + str(nKit).zfill(5)
	App.activeDocument().addObject("Part::Fuse",cFuse)
	App.activeDocument().getObject(cFuse).Base = App.activeDocument().getObject(cBase)
	App.activeDocument().getObject(cFuse).Tool = App.activeDocument().getObject(cTool)
	Gui.activeDocument().hide(cBase)
	Gui.activeDocument().hide(cTool)
	Gui.ActiveDocument.getObject(cFuse).ShapeColor=Gui.ActiveDocument.getObject(cBase).ShapeColor
	Gui.ActiveDocument.getObject(cFuse).DisplayMode=Gui.ActiveDocument.getObject(cBase).DisplayMode
	App.ActiveDocument.recompute()
	Gui.activeDocument().activeView().viewAxonometric()
	Gui.SendMsgToActiveView("ViewFit")
	kit0004(545, nLarg - 32) # -------------------------------------------------- Topo
	cBase = "Kit" + str(nKit).zfill(5)
	cTool = "Kit" + str(nKit).zfill(5)
	App.ActiveDocument.getObject(cTool).Placement = App.Placement(App.Vector(35, 16, 684),App.Rotation(App.Vector(0,0,1),0))
	nKit += 1
	cFuse = "Kit" + str(nKit).zfill(5)
	App.activeDocument().addObject("Part::Fuse",cFuse)
	App.activeDocument().getObject(cFuse).Base = App.activeDocument().getObject(cBase)
	App.activeDocument().getObject(cFuse).Tool = App.activeDocument().getObject(cTool)
	Gui.activeDocument().hide(cBase)
	Gui.activeDocument().hide(cTool)
	Gui.ActiveDocument.getObject(cFuse).ShapeColor=Gui.ActiveDocument.getObject(cBase).ShapeColor
	Gui.ActiveDocument.getObject(cFuse).DisplayMode=Gui.ActiveDocument.getObject(cBase).DisplayMode
	App.ActiveDocument.recompute()
	Gui.activeDocument().activeView().viewAxonometric()
	Gui.SendMsgToActiveView("ViewFit")

def kit0101(nLarg): # Movel Base c/prateleira
	if nLarg in range(300,601,50) + range(700,1201,100):
		global nKit
		kit0100(nLarg)		# Template MB
		kit0006(521, nLarg - 32) # -------------------------------------------------- Prateleira
		cBase = "Kit" + str(nKit).zfill(5)
		cTool = "Kit" + str(nKit).zfill(5)
		App.ActiveDocument.getObject(cTool).Placement = App.Placement(App.Vector(59, 16, 353),App.Rotation(App.Vector(0,0,1),0))
		nKit += 1
		cFuse = "Kit" + str(nKit).zfill(5)
		App.activeDocument().addObject("Part::Fuse",cFuse)
		App.activeDocument().getObject(cFuse).Base = App.activeDocument().getObject(cBase)
		App.activeDocument().getObject(cFuse).Tool = App.activeDocument().getObject(cTool)
		Gui.activeDocument().hide(cBase)
		Gui.activeDocument().hide(cTool)
		Gui.ActiveDocument.getObject(cFuse).ShapeColor=Gui.ActiveDocument.getObject(cBase).ShapeColor
		Gui.ActiveDocument.getObject(cFuse).DisplayMode=Gui.ActiveDocument.getObject(cBase).DisplayMode

def kit0102(nLarg): # Movel Base gavetas
	if nLarg in range(300,601,50):
		global nKit
		kit0100(nLarg)		# Template MB
		App.ActiveDocument.recompute()
		Gui.activeDocument().activeView().viewAxonometric()
		Gui.SendMsgToActiveView("ViewFit")

def kit0103(nLarg): # Movel Base lava-louça
	if nLarg in range(700,1201,100):
		global nKit
		kit0099(nLarg)
		kit0000(63, 16, nLarg - 32) # -------------------------------------------------- Regua trazeira superior
		cBase = "Kit" + str(nKit).zfill(5)
		cTool = "Kit" + str(nKit).zfill(5)
		App.ActiveDocument.getObject(cTool).Placement = App.Placement(App.Vector(0, 16, 700 - 63),App.Rotation(App.Vector(0,0,1),0))
		nKit += 1
		cFuse = "Kit" + str(nKit).zfill(5)
		App.activeDocument().addObject("Part::Fuse",cFuse)
		App.activeDocument().getObject(cFuse).Base = App.activeDocument().getObject(cBase)
		App.activeDocument().getObject(cFuse).Tool = App.activeDocument().getObject(cTool)
		Gui.activeDocument().hide(cBase)
		Gui.activeDocument().hide(cTool)
		Gui.ActiveDocument.getObject(cFuse).ShapeColor=Gui.ActiveDocument.getObject(cBase).ShapeColor
		Gui.ActiveDocument.getObject(cFuse).DisplayMode=Gui.ActiveDocument.getObject(cBase).DisplayMode
		kit0000(63, 16, nLarg - 32) # -------------------------------------------------- Regua trazeira inferior
		cBase = "Kit" + str(nKit).zfill(5)
		cTool = "Kit" + str(nKit).zfill(5)
		App.ActiveDocument.getObject(cTool).Placement = App.Placement(App.Vector(0, 16, 16),App.Rotation(App.Vector(0,0,1),0))
		nKit += 1
		cFuse = "Kit" + str(nKit).zfill(5)
		App.activeDocument().addObject("Part::Fuse",cFuse)
		App.activeDocument().getObject(cFuse).Base = App.activeDocument().getObject(cBase)
		App.activeDocument().getObject(cFuse).Tool = App.activeDocument().getObject(cTool)
		Gui.activeDocument().hide(cBase)
		Gui.activeDocument().hide(cTool)
		Gui.ActiveDocument.getObject(cFuse).ShapeColor=Gui.ActiveDocument.getObject(cBase).ShapeColor
		Gui.ActiveDocument.getObject(cFuse).DisplayMode=Gui.ActiveDocument.getObject(cBase).DisplayMode
		kit0000(63, 16, nLarg - 32) # -------------------------------------------------- Regua dianteira
		cBase = "Kit" + str(nKit).zfill(5)
		cTool = "Kit" + str(nKit).zfill(5)
		App.ActiveDocument.getObject(cTool).Placement = App.Placement(App.Vector(580 - 16, 16, 700 - 63),App.Rotation(App.Vector(0,0,1),0))
		nKit += 1
		cFuse = "Kit" + str(nKit).zfill(5)
		App.activeDocument().addObject("Part::Fuse",cFuse)
		App.activeDocument().getObject(cFuse).Base = App.activeDocument().getObject(cBase)
		App.activeDocument().getObject(cFuse).Tool = App.activeDocument().getObject(cTool)
		Gui.activeDocument().hide(cBase)
		Gui.activeDocument().hide(cTool)
		Gui.ActiveDocument.getObject(cFuse).ShapeColor=Gui.ActiveDocument.getObject(cBase).ShapeColor
		Gui.ActiveDocument.getObject(cFuse).DisplayMode=Gui.ActiveDocument.getObject(cBase).DisplayMode


def kit0104(nLarg): # Movel Base Forno
	if nLarg == 600:
		global nKit
		kit0001(700, 580)	# ------------------------------------------------ Ilharga esq.
		cBase = "Kit" + str(nKit).zfill(5)
		App.ActiveDocument.recompute()
		Gui.activeDocument().activeView().viewAxonometric()
		Gui.SendMsgToActiveView("ViewFit")
		kit0005(545, nLarg - 32)	# ------------------------------------------------ Base
		cTool = "Kit" + str(nKit).zfill(5)
		App.ActiveDocument.getObject(cTool).Placement = App.Placement(App.Vector(35, 16, 0),App.Rotation(App.Vector(0,0,1),0))
		nKit += 1
		cFuse = "Kit" + str(nKit).zfill(5)
		App.activeDocument().addObject("Part::Fuse",cFuse)
		App.activeDocument().getObject(cFuse).Base = App.activeDocument().getObject(cBase)
		App.activeDocument().getObject(cFuse).Tool = App.activeDocument().getObject(cTool)
		Gui.activeDocument().hide(cBase)
		Gui.activeDocument().hide(cTool)
		Gui.ActiveDocument.getObject(cFuse).ShapeColor=Gui.ActiveDocument.getObject(cBase).ShapeColor
		Gui.ActiveDocument.getObject(cFuse).DisplayMode=Gui.ActiveDocument.getObject(cBase).DisplayMode
		App.ActiveDocument.recompute()
		Gui.activeDocument().activeView().viewAxonometric()
		Gui.SendMsgToActiveView("ViewFit")
		kit0050(700, 580)	# ------------------------------------------------ Ilharga dir.
		cBase = "Kit" + str(nKit).zfill(5)
		cTool = "Kit" + str(nKit).zfill(5)
		App.ActiveDocument.getObject(cTool).Placement = App.Placement(App.Vector(0, nLarg - 16, 0),App.Rotation(App.Vector(0,0,1),0))
		nKit += 1
		cFuse = "Kit" + str(nKit).zfill(5)
		App.activeDocument().addObject("Part::Fuse",cFuse)
		App.activeDocument().getObject(cFuse).Base = App.activeDocument().getObject(cBase)
		App.activeDocument().getObject(cFuse).Tool = App.activeDocument().getObject(cTool)
		Gui.activeDocument().hide(cBase)
		Gui.activeDocument().hide(cTool)
		Gui.ActiveDocument.getObject(cFuse).ShapeColor=Gui.ActiveDocument.getObject(cBase).ShapeColor
		Gui.ActiveDocument.getObject(cFuse).DisplayMode=Gui.ActiveDocument.getObject(cBase).DisplayMode
		App.ActiveDocument.recompute()
		Gui.activeDocument().activeView().viewAxonometric()
		Gui.SendMsgToActiveView("ViewFit")
		kit0000(65, 521) # -------------------------------------------------- Regua p/Prateleira esq.
		cBase = "Kit" + str(nKit).zfill(5)
		cTool = "Kit" + str(nKit).zfill(5)
		App.ActiveDocument.getObject(cTool).Placement = App.Placement(App.Vector(59, 16, 16),App.Rotation(App.Vector(0,0,1),0))
		nKit += 1
		cFuse = "Kit" + str(nKit).zfill(5)
		App.activeDocument().addObject("Part::Fuse",cFuse)
		App.activeDocument().getObject(cFuse).Base = App.activeDocument().getObject(cBase)
		App.activeDocument().getObject(cFuse).Tool = App.activeDocument().getObject(cTool)
		Gui.activeDocument().hide(cBase)
		Gui.activeDocument().hide(cTool)
		Gui.ActiveDocument.getObject(cFuse).ShapeColor=Gui.ActiveDocument.getObject(cBase).ShapeColor
		Gui.ActiveDocument.getObject(cFuse).DisplayMode=Gui.ActiveDocument.getObject(cBase).DisplayMode
		kit0000(65, 521) # -------------------------------------------------- Regua p/Prateleira dir.
		cBase = "Kit" + str(nKit).zfill(5)
		cTool = "Kit" + str(nKit).zfill(5)
		App.ActiveDocument.getObject(cTool).Placement = App.Placement(App.Vector(59, 568, 16),App.Rotation(App.Vector(0,0,1),0))
		nKit += 1
		cFuse = "Kit" + str(nKit).zfill(5)
		App.activeDocument().addObject("Part::Fuse",cFuse)
		App.activeDocument().getObject(cFuse).Base = App.activeDocument().getObject(cBase)
		App.activeDocument().getObject(cFuse).Tool = App.activeDocument().getObject(cTool)
		Gui.activeDocument().hide(cBase)
		Gui.activeDocument().hide(cTool)
		Gui.ActiveDocument.getObject(cFuse).ShapeColor=Gui.ActiveDocument.getObject(cBase).ShapeColor
		Gui.ActiveDocument.getObject(cFuse).DisplayMode=Gui.ActiveDocument.getObject(cBase).DisplayMode
		kit0006(521, nLarg - 32) # -------------------------------------------------- Prateleira
		cBase = "Kit" + str(nKit).zfill(5)
		cTool = "Kit" + str(nKit).zfill(5)
		App.ActiveDocument.getObject(cTool).Placement = App.Placement(App.Vector(59, 16, 81),App.Rotation(App.Vector(0,0,1),0))
		nKit += 1
		cFuse = "Kit" + str(nKit).zfill(5)
		App.activeDocument().addObject("Part::Fuse",cFuse)
		App.activeDocument().getObject(cFuse).Base = App.activeDocument().getObject(cBase)
		App.activeDocument().getObject(cFuse).Tool = App.activeDocument().getObject(cTool)
		Gui.activeDocument().hide(cBase)
		Gui.activeDocument().hide(cTool)
		Gui.ActiveDocument.getObject(cFuse).ShapeColor=Gui.ActiveDocument.getObject(cBase).ShapeColor
		Gui.ActiveDocument.getObject(cFuse).DisplayMode=Gui.ActiveDocument.getObject(cBase).DisplayMode
		kit0000(90, 16, nLarg - 32) # -------------------------------------------------- Regua trazeira
		cBase = "Kit" + str(nKit).zfill(5)
		cTool = "Kit" + str(nKit).zfill(5)
		App.ActiveDocument.getObject(cTool).Placement = App.Placement(App.Vector(0, 16, 700 - 90),App.Rotation(App.Vector(0,0,1),0))
		nKit += 1
		cFuse = "Kit" + str(nKit).zfill(5)
		App.activeDocument().addObject("Part::Fuse",cFuse)
		App.activeDocument().getObject(cFuse).Base = App.activeDocument().getObject(cBase)
		App.activeDocument().getObject(cFuse).Tool = App.activeDocument().getObject(cTool)
		Gui.activeDocument().hide(cBase)
		Gui.activeDocument().hide(cTool)
		Gui.ActiveDocument.getObject(cFuse).ShapeColor=Gui.ActiveDocument.getObject(cBase).ShapeColor
		Gui.ActiveDocument.getObject(cFuse).DisplayMode=Gui.ActiveDocument.getObject(cBase).DisplayMode
		kit0000(19, 38, nLarg - 32) # -------------------------------------------------- Regua dianteira
		cBase = "Kit" + str(nKit).zfill(5)
		cTool = "Kit" + str(nKit).zfill(5)
		App.ActiveDocument.getObject(cTool).Placement = App.Placement(App.Vector(580 - 38, 16, 700 - 19),App.Rotation(App.Vector(0,0,1),0))
		nKit += 1
		cFuse = "Kit" + str(nKit).zfill(5)
		App.activeDocument().addObject("Part::Fuse",cFuse)
		App.activeDocument().getObject(cFuse).Base = App.activeDocument().getObject(cBase)
		App.activeDocument().getObject(cFuse).Tool = App.activeDocument().getObject(cTool)
		Gui.activeDocument().hide(cBase)
		Gui.activeDocument().hide(cTool)
		Gui.ActiveDocument.getObject(cFuse).ShapeColor=Gui.ActiveDocument.getObject(cBase).ShapeColor
		Gui.ActiveDocument.getObject(cFuse).DisplayMode=Gui.ActiveDocument.getObject(cBase).DisplayMode


nKit = 0					# Contagem de elementos
cKit = 0					# Elemento actual
nAgl = 16					# Espessura do aglomerado
nMB_alto = 700				# Altura dos MB's
nMB_largo = 580				# Profundidade dos MB´s
nMS_alto1 = 700				# Altura dos MS's normais
nMS_alto2 = 900				# Altura dos MS's especiais
nMS_largo = 330				# Profundidade dos MS's
nRas_alto = 8				# Profundidade dos rasgos para as costas
nRas_largo = 8				# Largura dos rasgos para as costas
nDis_dob = 37				# Distancia da frente para as dobradiças
nDis_Fdob = 32				# Distancia entre furos das dobradiças
nDis_Adob = 78				# Distancia do primeiro furo da dobradiça
nDis_prat = 37				# Distancia da frente para as prateleiras
ndis_Fprat = 64				# Distancia entre furos das prateleiras
nDis_Aprat = 222			# Distancia do primeiro furo da prateleira


#kit0100(200) # base (interno) a chamar por outros modulos
#kit0101(600) # c/prateleira
#kit0102(500) # gavetas
#kit0103(1200) # LL

#kit0000(700,580,19)
#kit0001(700,580)
#kit0002(700,580,2)
#kit0002(700,580)
#kit0003(468,545)
#kit0003(468,545,2)
#kit0006(700,580)
kit0100(400)

App.ActiveDocument.recompute()
Gui.activeDocument().activeView().viewAxonometric()
Gui.SendMsgToActiveView("ViewFit")
#exportViewToPNG()
