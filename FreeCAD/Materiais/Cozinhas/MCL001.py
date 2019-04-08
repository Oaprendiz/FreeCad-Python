# https://docs.python.org/3/extending/extending.html?highlight=true

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

import FreeCAD, Part, os

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

def Anime():
	App.ActiveDocument.recompute()
	Gui.activeDocument().activeView().viewAxonometric()
	Gui.SendMsgToActiveView("ViewFit")

def fusao(cBase, cTool):
	global nKit, cKit
	nKit +=1
	cKit = "Kit" + str(nKit).zfill(5)
	App.activeDocument().addObject("Part::Fuse", cKit)
	App.activeDocument().getObject(cKit).Base = App.activeDocument().getObject(cBase)
	App.activeDocument().getObject(cKit).Tool = App.activeDocument().getObject(cTool)
	Gui.activeDocument().hide(cBase)
	Gui.activeDocument().hide(cTool)
	Gui.ActiveDocument.getObject(cKit).ShapeColor=Gui.ActiveDocument.getObject(cBase).ShapeColor
	Gui.ActiveDocument.getObject(cKit).DisplayMode=Gui.ActiveDocument.getObject(cBase).DisplayMode

def cortar(cBase, cTool):
	global nKit, cKit
	nKit +=1
	cKit = "Kit" + str(nKit).zfill(5)
	App.activeDocument().addObject("Part::Cut", cKit)
	App.activeDocument().getObject(cKit).Base = App.activeDocument().getObject(cBase)
	App.activeDocument().getObject(cKit).Tool = App.activeDocument().getObject(cTool)
	Gui.activeDocument().hide(cBase)
	Gui.activeDocument().hide(cTool)
	Gui.ActiveDocument.getObject(cKit).ShapeColor=Gui.ActiveDocument.getObject(cBase).ShapeColor
	Gui.ActiveDocument.getObject(cKit).DisplayMode=Gui.ActiveDocument.getObject(cBase).DisplayMode

# ---------------------------------------- Elementos Básicos ----------------------------------------

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

def kit0007(nAlt, nLarg, nEsp = nAgl): # Ilharga Base lisa / Painel
	global nKit, cKit
	kit0000(nAlt, nLarg, nEsp)

def kit0008(nLarg, nFundo, nEsp = nAgl): # Prateleira Pentagonal
	global nKit, nKit
	nKit += 1
	cKit = "Kit" + str(nKit).zfill(5)
	pts=[]
	pts.append(App.Vector(0,0,0))
	pts.append(App.Vector(0, nFundo, 0))
	pts.append(App.Vector(nLarg, nFundo, 0))
	pts.append(App.Vector(nLarg, nFundo-nLarg, 0))
	pts.append(App.Vector(nLarg-nFundo, nFundo-nLarg,0))
	pts.append(App.Vector(0,0,0)) # make a closed polygon
	wire=Part.makePolygon(pts)
	face=Part.Face(wire)
	P = face.extrude(App.Vector(0,0,nAgl))
	App.ActiveDocument.addObject("Part::Feature", cKit)
	App.ActiveDocument.getObject(cKit).Shape = P

def kit0009(nLarg, nFundo, nPos = 1, nEsp = nAgl): # Topo e Base Pentagonal
	global nKit, nKit
	kit0008(nLarg, nFundo, nEsp)
	if nPos == 1:
		kit0050(nLarg, nFundo - 24, 3) # 1 = rasgo horizontal topo fundo
		kit0050(nLarg - 24, -(nLarg - nFundo), 5) # 1 = rasgo horizontal topo dir
	else:
		kit0050(nLarg, nFundo - 24, 4) # 2 = rasgo horizontal base fundo
		kit0050(nLarg - 24, -(nFundo - nLarg), 6) # 2 = rasgo horizontal topo dir

def kit0010(nAlt, nLarg, nFundo, nPos = 1): # Prumos para Cantos Pentagonais
	global nKit, cKit, nRas_alto, nRas_largo
	kit0000(nAlt, nFundo, nLarg)
#	kit0051(nAlt, 1)             # furos para dobradiças
	cBase = "Kit" + str(nKit).zfill(5)
	nKit += 1
	cKit = "Kit" + str(nKit).zfill(5)
	App.ActiveDocument.addObject("Part::Chamfer",cKit)
	App.ActiveDocument.getObject(cKit).Base = App.activeDocument().getObject(cBase)
	__fillets__ = []
	if nPos == 1:
		__fillets__.append((1,15.00,15.00))
	else:
		__fillets__.append((5,15.00,15.00))
	App.activeDocument().getObject(cKit).Edges = __fillets__
	del __fillets__
	Gui.activeDocument().hide(cBase)
	Gui.ActiveDocument.getObject(cKit).ShapeColor=Gui.ActiveDocument.getObject(cBase).ShapeColor
	Gui.ActiveDocument.getObject(cKit).DisplayMode=Gui.ActiveDocument.getObject(cBase).DisplayMode

def kit0011(nLarg, nFundo, nEsp = nAgl): # Prateleira L
	global nKit, nKit
	nKit += 1
	cKit = "Kit" + str(nKit).zfill(5)
	pts=[]
	pts.append(App.Vector(0,0,0))
	pts.append(App.Vector(0, nFundo, 0))
	pts.append(App.Vector(nLarg, nFundo, 0))
	pts.append(App.Vector(nLarg, nFundo-nLarg, 0))
	pts.append(App.Vector(nLarg-nFundo, nFundo-nLarg,0))
	pts.append(App.Vector(nLarg-nFundo, 0,0))
	pts.append(App.Vector(0,0,0)) # make a closed polygon
	wire=Part.makePolygon(pts)
	face=Part.Face(wire)
	P = face.extrude(App.Vector(0,0,nAgl))
	App.ActiveDocument.addObject("Part::Feature", cKit)
	App.ActiveDocument.getObject(cKit).Shape = P

def kit0012(nLarg, nFundo, nPos = 1, nEsp = nAgl): # Topo e Base L
	global nKit, nKit
	kit0011(nLarg, nFundo, nEsp)
	if nPos == 1:
		kit0050(nLarg, nFundo - 24, 3) # 1 = rasgo horizontal topo fundo
		kit0050(nLarg - 24, -(nLarg - nFundo), 5) # 1 = rasgo horizontal topo dir
	else:
		kit0050(nLarg, nFundo - 24, 4) # 2 = rasgo horizontal base fundo
		kit0050(nLarg - 24, -(nFundo - nLarg), 6) # 2 = rasgo horizontal topo dir

# ---------------------------------------- Componentes / Acessórios ----------------------------------------


def kit0050(nDim, nDis, nPos = 1): # Rasgo para as costas ou fundo de gavetas
	if nPos in range(1, 7):
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
				App.ActiveDocument.getObject(cKit).Placement = App.Placement(App.Vector(nRas_alto, nDis, 0),App.Rotation(App.Vector(0, 0, 1),0))
			else:
				App.ActiveDocument.getObject(cKit).Placement = App.Placement(App.Vector(0, nDis, 0),App.Rotation(App.Vector(0,0,1),0))
		elif nPos == 3 or nPos ==4: # horizontal topo/base
			App.ActiveDocument.getObject(cKit).Height = str(nRas_largo) + ' mm'
			App.ActiveDocument.getObject(cKit).Width = str(nRas_alto) + ' mm'
			App.ActiveDocument.getObject(cKit).Length = str(nDim) + ' mm'
			if nPos == 3:
				App.ActiveDocument.getObject(cKit).Placement = App.Placement(App.Vector(0, nDis, 0),App.Rotation(App.Vector(0, 0, 1),0))
			else:
				App.ActiveDocument.getObject(cKit).Placement = App.Placement(App.Vector(0, nDis, nRas_alto),App.Rotation(App.Vector(0,0,1),0))
		elif nPos == 5 or nPos ==6: # horizontal esq/dir
			App.ActiveDocument.getObject(cKit).Height = str(nRas_largo) + ' mm'
			App.ActiveDocument.getObject(cKit).Width = str(nDim) + ' mm'
			App.ActiveDocument.getObject(cKit).Length = str(nRas_alto) + ' mm'
			if nPos == 5:
				App.ActiveDocument.getObject(cKit).Placement = App.Placement(App.Vector(nDim, -nDis, 0),App.Rotation(App.Vector(0, 0, 1),0))
			else:
				App.ActiveDocument.getObject(cKit).Placement = App.Placement(App.Vector(nDim, -nDis, nRas_alto),App.Rotation(App.Vector(0,0,1),0))
		cTool = cKit
		cortar(cBase, cTool)

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
			cortar(cBase, cTool)
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
			cortar(cBase, cTool)

def kit0052(nAlt, nPos): # Furo para optimização
	global nCylinder, nKit
	cFuro = "Cylinder" + str(nCylinder).zfill(5)
	nCylinder += 1
	App.ActiveDocument.addObject("Part::Cylinder",cFuro)
	App.ActiveDocument.getObject(cFuro).Radius = '2,5 mm'
	App.ActiveDocument.getObject(cFuro).Height = '8 mm'
	App.ActiveDocument.getObject(cFuro).Placement = App.Placement(App.Vector(x, z, y),App.Rotation(App.Vector(0,1,0),90))

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
			cortar(cBase, cTool)


# ---------------------------------------- Kit's de Cozinha ----------------------------------------


def kit0100(nLarg): # Movel Base s/prateleira (modelo para todos os MB's)
	global nKit, cKit
	kit0002(nMB_alto, nMB_fundo, 1)	# ------------------------------------------------ Ilharga esq.
	if lAnime: Anime()
	cBase = "Kit" + str(nKit).zfill(5)
	kit0005(nMB_alto - nAgl, nLarg - nAgl)	# ---------------------------------------- Costas
	cTool = "Kit" + str(nKit).zfill(5)
	App.ActiveDocument.getObject(cTool).Placement = App.Placement(App.Vector(nAgl/2,nMB_fundo-59,nAgl/2),App.Rotation(App.Vector(0,0,1),0))
	if lAnime: Anime()
	fusao(cBase, cTool)
	cBase = "Kit" + str(nKit).zfill(5)
	kit0002(nMB_alto, nMB_fundo, 2)	# ------------------------------------------------ Ilharga dir.
	cTool = "Kit" + str(nKit).zfill(5)
	App.ActiveDocument.getObject(cTool).Placement = App.Placement(App.Vector(nLarg - nAgl, 0, 0),App.Rotation(App.Vector(0,0,1),0))
	if lAnime: Anime()
	fusao(cBase, cTool)
	cBase = "Kit" + str(nKit).zfill(5)
	kit0003(nLarg - nAgl*2, nMB_fundo-35, 2)	# ------------------------------------------------ Base
	cTool = "Kit" + str(nKit).zfill(5)
	App.ActiveDocument.getObject(cTool).Placement = App.Placement(App.Vector(nAgl, 0, 0),App.Rotation(App.Vector(0,0,1),0))
	if lAnime: Anime()
	fusao(cBase, cTool)
	cBase = "Kit" + str(nKit).zfill(5)
	kit0003(nLarg - nAgl*2, nMB_fundo-35) # -------------------------------------------------- Topo
	cTool = "Kit" + str(nKit).zfill(5)
	App.ActiveDocument.getObject(cTool).Placement = App.Placement(App.Vector(nAgl, 0, nMB_alto-nAgl),App.Rotation(App.Vector(0,0,1),0))
	if lAnime: Anime()
	fusao(cBase, cTool)

def kit0101(nLarg): # Movel Base c/prateleira
	if nLarg in range(300,601,50) + range(700,1201,100):
		global nKit, cKit
		kit0100(nLarg)		# Template MB
		cBase = "Kit" + str(nKit).zfill(5)
		kit0006(nLarg - nAgl*2, nMB_fundo-59) # -------------------------------------------------- Prateleira
		cTool = "Kit" + str(nKit).zfill(5)
		App.ActiveDocument.getObject(cTool).Placement = App.Placement(App.Vector(nAgl, 0, nMB_alto/2),App.Rotation(App.Vector(0,0,1),0))
		if lAnime: Anime()
		fusao(cBase, cTool)

def kit0102(nLarg): # Movel Base gavetas
	if nLarg in range(300,601,50):
		global nKit
		kit0100(nLarg)		# Template MB
		if lAnime: Anime()

def kit0103(nLarg): # Movel Base lava-louça
	global nKit, cKit
	if nLarg in [600, 800, 900, 1000, 1100, 1200]:
		kit0004(nMB_alto, nMB_fundo, 1)	# ---------------------------------------------- Ilharga esq.
		cBase = "Kit" + str(nKit).zfill(5)
		kit0000(63, nAgl, nLarg - nAgl*2) # -------------------------------------------------- Regua trazeira superior
		cTool = "Kit" + str(nKit).zfill(5)
		App.ActiveDocument.getObject(cTool).Placement = App.Placement(App.Vector(nAgl, nMB_fundo-nAgl, nMB_alto - 63),App.Rotation(App.Vector(0,0,1),0))
		if lAnime: Anime()
		fusao(cBase, cTool)
		cBase = "Kit" + str(nKit).zfill(5)
		kit0000(63, nAgl, nLarg - nAgl*2) # -------------------------------------------------- Regua trazeira inferior
		cTool = "Kit" + str(nKit).zfill(5)
		App.ActiveDocument.getObject(cTool).Placement = App.Placement(App.Vector(nAgl, nMB_fundo-nAgl, nAgl),App.Rotation(App.Vector(0,0,1),0))
		if lAnime: Anime()
		fusao(cBase, cTool)
		cBase = "Kit" + str(nKit).zfill(5)
		kit0000(63, nAgl, nLarg - nAgl*2) # -------------------------------------------------- Regua dianteira
		cTool = "Kit" + str(nKit).zfill(5)
		App.ActiveDocument.getObject(cTool).Placement = App.Placement(App.Vector(nAgl, 0, nMB_alto - 63),App.Rotation(App.Vector(0,0,1),0))
		if lAnime: Anime()
		fusao(cBase, cTool)
		cBase = "Kit" + str(nKit).zfill(5)
		kit0006(nLarg - nAgl*2, nMB_fundo) # -------------------------------------------------- Base
		cTool = "Kit" + str(nKit).zfill(5)
		App.ActiveDocument.getObject(cTool).Placement = App.Placement(App.Vector(nAgl, 0, 0),App.Rotation(App.Vector(0,0,1),0))
		if lAnime: Anime()
		fusao(cBase, cTool)
		cBase = "Kit" + str(nKit).zfill(5)
		kit0004(nMB_alto, nMB_fundo, 2)	# ---------------------------------------------- Ilharga dir.
		cTool = "Kit" + str(nKit).zfill(5)
		App.ActiveDocument.getObject(cTool).Placement = App.Placement(App.Vector(nLarg-nAgl, 0, 0),App.Rotation(App.Vector(0,0,1),0))
		if lAnime: Anime()
		fusao(cBase, cTool)

def kit0104(nLarg): # Movel Base Forno
	if nLarg == 600:
		global nKit, cKit
		kit0007(nMB_alto, nMB_fundo)	# ------------------------------------------------ Ilharga
		if lAnime: Anime()
		cBase = "Kit" + str(nKit).zfill(5)
		kit0006(nLarg - nAgl*2, nMB_fundo)	# ------------------------------------------------ Base
		cTool = "Kit" + str(nKit).zfill(5)
		if lAnime: Anime()
		fusao(cBase, cTool)
		cBase = "Kit" + str(nKit).zfill(5)
		kit0007(nMB_alto, nMB_fundo)	# ------------------------------------------------ Ilharga
		cTool = "Kit" + str(nKit).zfill(5)
		App.ActiveDocument.getObject(cTool).Placement = App.Placement(App.Vector(nLarg - nAgl, 0, 0),App.Rotation(App.Vector(0,0,1),0))
		if lAnime: Anime()
		fusao(cBase, cTool)
		cBase = "Kit" + str(nKit).zfill(5)
		kit0007(65, nMB_fundo) # -------------------------------------------------- Regua p/Prateleira esq.
		cTool = "Kit" + str(nKit).zfill(5)
		App.ActiveDocument.getObject(cTool).Placement = App.Placement(App.Vector(nAgl, 0, nAgl),App.Rotation(App.Vector(0,0,1),0))
		if lAnime: Anime()
		fusao(cBase, cTool)
		cBase = "Kit" + str(nKit).zfill(5)
		kit0007(65, nMB_fundo) # -------------------------------------------------- Regua p/Prateleira dir.
		cTool = "Kit" + str(nKit).zfill(5)
		App.ActiveDocument.getObject(cTool).Placement = App.Placement(App.Vector(nLarg-nAgl*2, 0, nAgl),App.Rotation(App.Vector(0,0,1),0))
		if lAnime: Anime()
		fusao(cBase, cTool)
		cBase = "Kit" + str(nKit).zfill(5)
		kit0006(nLarg - nAgl*2, nMB_fundo) # -------------------------------------------------- Prateleira
		cTool = "Kit" + str(nKit).zfill(5)
		App.ActiveDocument.getObject(cTool).Placement = App.Placement(App.Vector(nAgl, 0, 65+nAgl),App.Rotation(App.Vector(0,0,1),0))
		if lAnime: Anime()
		fusao(cBase, cTool)
		cBase = "Kit" + str(nKit).zfill(5)
		kit0000(90, nAgl, nLarg - nAgl*2) # -------------------------------------------------- Regua trazeira
		cTool = "Kit" + str(nKit).zfill(5)
		App.ActiveDocument.getObject(cTool).Placement = App.Placement(App.Vector(nAgl, nMB_fundo-nAgl, nMB_alto - 90),App.Rotation(App.Vector(0,0,1),0))
		if lAnime: Anime()
		fusao(cBase, cTool)
		cBase = "Kit" + str(nKit).zfill(5)
		kit0000(nAgl, 38, nLarg - nAgl*2) # -------------------------------------------------- Regua dianteira
		cTool = "Kit" + str(nKit).zfill(5)
		App.ActiveDocument.getObject(cTool).Placement = App.Placement(App.Vector(nAgl, 0, nMB_alto - nAgl),App.Rotation(App.Vector(0,0,1),0))
		if lAnime: Anime()
		fusao(cBase, cTool)

def kit0105(nLarg): # Movel Base Canto Pentagono
	if nLarg == 950:
		global nKit, cKit
		kit0002(nMB_alto, nMB_fundo)	# ------------------------------------------------ Ilharga esq.
		cBase = "Kit" + str(nKit).zfill(5)
		if lAnime: Anime()
		kit0009(nLarg - nAgl-35, nMB_fundo-35, 2)	# ------------------------------------------------ Base
		cTool = "Kit" + str(nKit).zfill(5)
		App.ActiveDocument.getObject(cTool).Placement = App.Placement(App.Vector(nAgl, 0, 0),App.Rotation(App.Vector(0,0,1),0))
		if lAnime: Anime()
		fusao(cBase, cTool)
		cBase = "Kit" + str(nKit).zfill(5)
		kit0002(nMB_alto, nMB_fundo, 2)	# ------------------------------------------------ Ilharga dir.
		cTool = "Kit" + str(nKit).zfill(5)
		App.ActiveDocument.getObject(cTool).Placement = App.Placement(App.Vector(nLarg - nMB_fundo, nMB_fundo - nLarg + nAgl, 0),App.Rotation(App.Vector(0,0,1),270))
		if lAnime: Anime()
		fusao(cBase, cTool)
		cBase = "Kit" + str(nKit).zfill(5)
		kit0009(nLarg - nAgl-35, nMB_fundo-35)	# ------------------------------------------------ topo
		cTool = "Kit" + str(nKit).zfill(5)
		App.ActiveDocument.getObject(cTool).Placement = App.Placement(App.Vector(nAgl, 0, nMB_alto-nAgl),App.Rotation(App.Vector(0,0,1),0))
		if lAnime: Anime()
		fusao(cBase, cTool)
		cBase = "Kit" + str(nKit).zfill(5)
		kit0010(nMB_alto - nAgl*2, 30, 60)	# ------------------------------------------------ Prumo esq.
		cTool = "Kit" + str(nKit).zfill(5)
		App.ActiveDocument.getObject(cTool).Placement = App.Placement(App.Vector(6, 12, nAgl),App.Rotation(App.Vector(0,0,1),315))
		if lAnime: Anime()
		fusao(cBase, cTool)
		cBase = "Kit" + str(nKit).zfill(5)
		kit0010(nMB_alto - nAgl*2, 30, 60, 2)	# ------------------------------------------------ Prumo esq.
		cTool = "Kit" + str(nKit).zfill(5)
#		App.ActiveDocument.getObject(cTool).Placement = App.Placement(App.Vector(nLarg - nMB_fundo-16, nMB_fundo - nLarg +47, nAgl),App.Rotation(App.Vector(0,0,1),315))
		App.ActiveDocument.getObject(cTool).Placement = App.Placement(App.Vector(360,-344, nAgl),App.Rotation(App.Vector(0,0,1),315))
		if lAnime: Anime()
		fusao(cBase, cTool)
		cBase = "Kit" + str(nKit).zfill(5)
		kit0008(nLarg - nAgl-60, nMB_fundo-147, 2)	# ------------------------------------------------ Prateleira
		cTool = "Kit" + str(nKit).zfill(5)
		App.ActiveDocument.getObject(cTool).Placement = App.Placement(App.Vector(nAgl, 88, nMB_alto/2),App.Rotation(App.Vector(0,0,1),0))
		if lAnime: Anime()
		fusao(cBase, cTool)
		cBase = "Kit" + str(nKit).zfill(5)
		kit0005(nMB_alto - nAgl, nLarg - nAgl-35-nAgl)	# ---------------------------------------- Costas
		cTool = "Kit" + str(nKit).zfill(5)
		App.ActiveDocument.getObject(cTool).Placement = App.Placement(App.Vector(nAgl/2,nMB_fundo-59,nAgl/2),App.Rotation(App.Vector(0,0,1),0))
		if lAnime: Anime()
		fusao(cBase, cTool)
		cBase = "Kit" + str(nKit).zfill(5)
		kit0005(nMB_alto - nAgl, nLarg - nAgl-35-nAgl)	# ---------------------------------------- Costas
		cTool = "Kit" + str(nKit).zfill(5)
		App.ActiveDocument.getObject(cTool).Placement = App.Placement(App.Vector(nLarg - nAgl/2-35-nAgl,nMB_fundo-59,nAgl/2),App.Rotation(App.Vector(0,0,1),270))



App.newDocument("Sem nome")
lAnime = True
nKit = 0					# Contagem de elementos
cKit = 0					# Elemento actual
nAgl = 16					# Espessura do aglomerado
nMB_alto = 700				# Altura dos MB's
nMB_fundo = 580				# Profundidade dos MB´s
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
#kit0005(700,580)
#kit0103(1200)
#kit0104(600)
#kit0009(900,580,2)
#kit0010(700,30,60)
#kit0100(900)
#kit0011(950,580)
kit0105(950)


App.ActiveDocument.recompute()
Gui.activeDocument().activeView().viewAxonometric()
Gui.SendMsgToActiveView("ViewFit")
#exportViewToPNG()
