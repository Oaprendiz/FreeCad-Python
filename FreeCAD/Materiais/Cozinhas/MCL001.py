
def kit0000(nAlt, nLarg, nEsp = nAgl): # Ilharga Base lisa
	global nBox
	nBox += 1
	cBox = "Box" + str(nBox).zfill(5)
	App.ActiveDocument.addObject("Part::Box", cBox)
	App.ActiveDocument.getObject(cBox).Height = str(nAlt) + ' mm'
	App.ActiveDocument.getObject(cBox).Width = str(nLarg) + ' mm'
	App.ActiveDocument.getObject(cBox).Length = str(nEsp) + ' mm'

def kit0001(nAlt, nLarg, nEsp = nAgl): # Ilharga Base c/rasgo e furação esq.
	global nBox, nCut
	kit0000(nAlt, nLarg, nEsp)
	cBase = "Box" + str(nBox).zfill(5)
	nBox += 1
	cBox = "Box" + str(nBox).zfill(5)
	App.ActiveDocument.addObject("Part::Box", cBox)
	App.ActiveDocument.getObject(cBox).Height = str(nAlt) + ' mm'
	App.ActiveDocument.getObject(cBox).Width = '8 mm'
	App.ActiveDocument.getObject(cBox).Length = '8 mm'
	App.ActiveDocument.getObject(cBox).Placement = App.Placement(App.Vector(8, nLarg - 51, 0),App.Rotation(App.Vector(0, 0, 1),0))
	
	nCut +=1
	cCut = "Cut" + str(nCut).zfill(5)
	App.activeDocument().addObject("Part::Cut", cCut)
	App.activeDocument().getObject(cCut).Base = App.activeDocument().getObject(cBase)
	App.activeDocument().getObject(cCut).Tool = App.activeDocument().getObject(cBox)
	Gui.activeDocument().hide(cBase)
	Gui.activeDocument().hide(cBox)
	Gui.ActiveDocument.getObject(cCut).ShapeColor=Gui.ActiveDocument.getObject(cBase).ShapeColor
	Gui.ActiveDocument.getObject(cCut).DisplayMode=Gui.ActiveDocument.getObject(cBase).DisplayMode
	
	for n in range(0, 5):	# furos p/prateleira
		kit0003(8, 37, 222 + n * 64)
		kit0003(8, 460, 222 + n * 64)

			# furos p/dobradiças
	kit0003(8, 37, 78), kit0003(8, 37, 112)
	kit0003(8, 37, 622), kit0003(8, 37, 590)

def kit0002(nAlt, nLarg, nEsp = nAgl): # Ilharga Base c/rasgo e furação dir.
	global nBox, nCut
	kit0000(nAlt, nLarg, nEsp)
	cBase = "Box" + str(nBox).zfill(5)
	nBox += 1
	cBox = "Box" + str(nBox).zfill(5)
	App.ActiveDocument.addObject("Part::Box", cBox)
	App.ActiveDocument.getObject(cBox).Height = str(nAlt) + ' mm'
	App.ActiveDocument.getObject(cBox).Width = '8 mm'
	App.ActiveDocument.getObject(cBox).Length = '8 mm'
	App.ActiveDocument.getObject(cBox).Placement = App.Placement(App.Vector(51,0,0),App.Rotation(App.Vector(0,0,1),0))
	
	nCut +=1
	cCut = "Cut" + str(nCut).zfill(5)
	App.activeDocument().addObject("Part::Cut", cCut)
	App.activeDocument().getObject(cCut).Base = App.activeDocument().getObject(cBase)
	App.activeDocument().getObject(cCut).Tool = App.activeDocument().getObject(cBox)
	Gui.activeDocument().hide(cBase)
	Gui.activeDocument().hide(cBox)
	Gui.ActiveDocument.getObject(cCut).ShapeColor=Gui.ActiveDocument.getObject(cBase).ShapeColor
	Gui.ActiveDocument.getObject(cCut).DisplayMode=Gui.ActiveDocument.getObject(cBase).DisplayMode
	
	for n in range(0, 5):	# furos p/prateleira
		kit0003(543, 0, 222 + n * 64)
		kit0003(120, 0, 222 + n * 64)

			# furos p/dobradiças
	kit0003(543, 0, 78), kit0003(543, 0, 112)
	kit0003(543, 0, 622), kit0003(543, 0, 590)

def kit0003(x, z, y): # Furo para prateleiras
	global nCylinder, nCut
	cFuro = "Cylinder" + str(nCylinder).zfill(5)
	nCylinder += 1
	App.ActiveDocument.addObject("Part::Cylinder",cFuro)
	App.ActiveDocument.getObject(cFuro).Radius = '2,5 mm'
	App.ActiveDocument.getObject(cFuro).Height = '8 mm'
	App.ActiveDocument.getObject(cFuro).Placement = App.Placement(App.Vector(x, z, y),App.Rotation(App.Vector(0,1,0),90))

#	cBase = "Cut" + str(nCut).zfill(5)
#	nCut +=1
#	cCut = "Cut" + str(nCut).zfill(5)
#	App.activeDocument().addObject("Part::Cut", cCut)
#	App.activeDocument().getObject(cCut).Base = App.activeDocument().getObject(cBase)
#	App.activeDocument().getObject(cCut).Tool = App.activeDocument().getObject(cFuro)
#	Gui.activeDocument().hide(cBase)
#	Gui.activeDocument().hide(cFuro)
#	Gui.ActiveDocument.getObject(cCut).ShapeColor=Gui.ActiveDocument.getObject(cBase).ShapeColor
#	Gui.ActiveDocument.getObject(cCut).DisplayMode=Gui.ActiveDocument.getObject(cBase).DisplayMode

def kit0004(nAlt, nLarg, nEsp = nAgl): # Topo MB
	global nBox, nCut
	nBox += 1
	cBox = "Box" + str(nBox).zfill(5)
	App.ActiveDocument.addObject("Part::Box", cBox)
	App.ActiveDocument.getObject(cBox).Height = str(nEsp) + ' mm'
	App.ActiveDocument.getObject(cBox).Width = str(nLarg) + ' mm'
	App.ActiveDocument.getObject(cBox).Length = str(nAlt) + ' mm'
	cBase = "Box" + str(nBox).zfill(5)
	nBox += 1
	cBox = "Box" + str(nBox).zfill(5)
	App.ActiveDocument.addObject("Part::Box", cBox)
	App.ActiveDocument.getObject(cBox).Height = '8 mm'
	App.ActiveDocument.getObject(cBox).Width = str(nLarg) + ' mm'
	App.ActiveDocument.getObject(cBox).Length = '8 mm'
	App.ActiveDocument.getObject(cBox).Placement = App.Placement(App.Vector(16,0,0),App.Rotation(App.Vector(0,0,1),0))
	
	nCut +=1
	cCut = "Cut" + str(nCut).zfill(5)
	App.activeDocument().addObject("Part::Cut", cCut)
	App.activeDocument().getObject(cCut).Base = App.activeDocument().getObject(cBase)
	App.activeDocument().getObject(cCut).Tool = App.activeDocument().getObject(cBox)
	Gui.activeDocument().hide(cBase)
	Gui.activeDocument().hide(cBox)
	Gui.ActiveDocument.getObject(cCut).ShapeColor=Gui.ActiveDocument.getObject(cBase).ShapeColor
	Gui.ActiveDocument.getObject(cCut).DisplayMode=Gui.ActiveDocument.getObject(cBase).DisplayMode

def kit0005(nAlt, nLarg, nEsp = nAgl): # Fundo MB
	global nBox, nCut
	nBox += 1
	cBox = "Box" + str(nBox).zfill(5)
	App.ActiveDocument.addObject("Part::Box", cBox)
	App.ActiveDocument.getObject(cBox).Height = str(nEsp) + ' mm'
	App.ActiveDocument.getObject(cBox).Width = str(nLarg) + ' mm'
	App.ActiveDocument.getObject(cBox).Length = str(nAlt) + ' mm'
	cBase = "Box" + str(nBox).zfill(5)
	nBox += 1
	cBox = "Box" + str(nBox).zfill(5)
	App.ActiveDocument.addObject("Part::Box", cBox)
	App.ActiveDocument.getObject(cBox).Height = '8 mm'
	App.ActiveDocument.getObject(cBox).Width = str(nLarg) + ' mm'
	App.ActiveDocument.getObject(cBox).Length = '8 mm'
	App.ActiveDocument.getObject(cBox).Placement = App.Placement(App.Vector(16,0,8),App.Rotation(App.Vector(0,0,1),0))
	
	nCut +=1
	cCut = "Cut" + str(nCut).zfill(5)
	App.activeDocument().addObject("Part::Cut", cCut)
	App.activeDocument().getObject(cCut).Base = App.activeDocument().getObject(cBase)
	App.activeDocument().getObject(cCut).Tool = App.activeDocument().getObject(cBox)
	Gui.activeDocument().hide(cBase)
	Gui.activeDocument().hide(cBox)
	Gui.ActiveDocument.getObject(cCut).ShapeColor=Gui.ActiveDocument.getObject(cBase).ShapeColor
	Gui.ActiveDocument.getObject(cCut).DisplayMode=Gui.ActiveDocument.getObject(cBase).DisplayMode

def kit0006(nAlt, nLarg, nEsp = nAgl): # Prateleira Base
	global nBox
	nBox += 1
	cBox = "Box" + str(nBox).zfill(5)
	App.ActiveDocument.addObject("Part::Box", cBox)
	App.ActiveDocument.getObject(cBox).Height = str(nEsp) + ' mm'
	App.ActiveDocument.getObject(cBox).Width = str(nLarg) + ' mm'
	App.ActiveDocument.getObject(cBox).Length = str(nAlt) + ' mm'

def kit0007(nAlt, nLarg, nEsp = 8): # Costa Base
	global nBox
	nBox += 1
	cBox = "Box" + str(nBox).zfill(5)
	App.ActiveDocument.addObject("Part::Box", cBox)
	App.ActiveDocument.getObject(cBox).Height = str(nAlt) + ' mm'
	App.ActiveDocument.getObject(cBox).Width = str(nLarg) + ' mm'
	App.ActiveDocument.getObject(cBox).Length = str(nEsp) + ' mm'

def kit0099(nLarg): # Movel Base s/Topo (modelo pada MB's forno e LL
	global nFuse
	kit0001(700, 580)	# ------------------------------------------------ Ilharga esq.
	cBase = "Cut" + str(nCut).zfill(5)
	App.ActiveDocument.recompute()
	Gui.activeDocument().activeView().viewAxonometric()
	Gui.SendMsgToActiveView("ViewFit")
	kit0005(545, nLarg - 32)	# ------------------------------------------------ Base
	cTool = "Cut" + str(nCut).zfill(5)
	App.ActiveDocument.getObject(cTool).Placement = App.Placement(App.Vector(35, 16, 0),App.Rotation(App.Vector(0,0,1),0))
	nFuse += 1
	cFuse = "Fuse" + str(nFuse).zfill(5)
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
	kit0002(700, 580)	# ------------------------------------------------ Ilharga dir.
	cBase = "Fuse" + str(nFuse).zfill(5)
	cTool = "Cut" + str(nCut).zfill(5)
	App.ActiveDocument.getObject(cTool).Placement = App.Placement(App.Vector(0, nLarg - 16, 0),App.Rotation(App.Vector(0,0,1),0))
	nFuse += 1
	cFuse = "Fuse" + str(nFuse).zfill(5)
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
	global nFuse
	kit0001(700, 580)	# ------------------------------------------------ Ilharga esq.
	cBase = "Cut" + str(nCut).zfill(5)
	App.ActiveDocument.recompute()
	Gui.activeDocument().activeView().viewAxonometric()
	Gui.SendMsgToActiveView("ViewFit")
	kit0007(684, nLarg - 16)	# ---------------------------------------- Costas
	cTool = "Box" + str(nBox).zfill(5)
	App.ActiveDocument.getObject(cTool).Placement = App.Placement(App.Vector(51,8,8),App.Rotation(App.Vector(0,0,1),0))
	nFuse += 1
	cFuse = "Fuse" + str(nFuse).zfill(5)
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
	kit0002(700, 580)	# ------------------------------------------------ Ilharga dir.
	cBase = "Fuse" + str(nFuse).zfill(5)
	cTool = "Cut" + str(nCut).zfill(5)
	App.ActiveDocument.getObject(cTool).Placement = App.Placement(App.Vector(0, nLarg - 16, 0),App.Rotation(App.Vector(0,0,1),0))
	nFuse += 1
	cFuse = "Fuse" + str(nFuse).zfill(5)
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
	cBase = "Fuse" + str(nFuse).zfill(5)
	cTool = "Cut" + str(nCut).zfill(5)
	App.ActiveDocument.getObject(cTool).Placement = App.Placement(App.Vector(35, 16, 0),App.Rotation(App.Vector(0,0,1),0))
	nFuse += 1
	cFuse = "Fuse" + str(nFuse).zfill(5)
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
	cBase = "Fuse" + str(nFuse).zfill(5)
	cTool = "Cut" + str(nCut).zfill(5)
	App.ActiveDocument.getObject(cTool).Placement = App.Placement(App.Vector(35, 16, 684),App.Rotation(App.Vector(0,0,1),0))
	nFuse += 1
	cFuse = "Fuse" + str(nFuse).zfill(5)
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
		global nFuse
		kit0100(nLarg)		# Template MB
		kit0006(521, nLarg - 32) # -------------------------------------------------- Prateleira
		cBase = "Fuse" + str(nFuse).zfill(5)
		cTool = "Box" + str(nBox).zfill(5)
		App.ActiveDocument.getObject(cTool).Placement = App.Placement(App.Vector(59, 16, 353),App.Rotation(App.Vector(0,0,1),0))
		nFuse += 1
		cFuse = "Fuse" + str(nFuse).zfill(5)
		App.activeDocument().addObject("Part::Fuse",cFuse)
		App.activeDocument().getObject(cFuse).Base = App.activeDocument().getObject(cBase)
		App.activeDocument().getObject(cFuse).Tool = App.activeDocument().getObject(cTool)
		Gui.activeDocument().hide(cBase)
		Gui.activeDocument().hide(cTool)
		Gui.ActiveDocument.getObject(cFuse).ShapeColor=Gui.ActiveDocument.getObject(cBase).ShapeColor
		Gui.ActiveDocument.getObject(cFuse).DisplayMode=Gui.ActiveDocument.getObject(cBase).DisplayMode

def kit0102(nLarg): # Movel Base gavetas
	if nLarg in range(300,601,50):
		global nFuse
		kit0100(nLarg)		# Template MB
		App.ActiveDocument.recompute()
		Gui.activeDocument().activeView().viewAxonometric()
		Gui.SendMsgToActiveView("ViewFit")

def kit0103(nLarg): # Movel Base lava-louça
	if nLarg in range(700,1201,100):
		global nFuse
		kit0099(nLarg)
		kit0000(63, 16, nLarg - 32) # -------------------------------------------------- Regua trazeira superior
		cBase = "Fuse" + str(nFuse).zfill(5)
		cTool = "Box" + str(nBox).zfill(5)
		App.ActiveDocument.getObject(cTool).Placement = App.Placement(App.Vector(0, 16, 700 - 63),App.Rotation(App.Vector(0,0,1),0))
		nFuse += 1
		cFuse = "Fuse" + str(nFuse).zfill(5)
		App.activeDocument().addObject("Part::Fuse",cFuse)
		App.activeDocument().getObject(cFuse).Base = App.activeDocument().getObject(cBase)
		App.activeDocument().getObject(cFuse).Tool = App.activeDocument().getObject(cTool)
		Gui.activeDocument().hide(cBase)
		Gui.activeDocument().hide(cTool)
		Gui.ActiveDocument.getObject(cFuse).ShapeColor=Gui.ActiveDocument.getObject(cBase).ShapeColor
		Gui.ActiveDocument.getObject(cFuse).DisplayMode=Gui.ActiveDocument.getObject(cBase).DisplayMode
		kit0000(63, 16, nLarg - 32) # -------------------------------------------------- Regua trazeira inferior
		cBase = "Fuse" + str(nFuse).zfill(5)
		cTool = "Box" + str(nBox).zfill(5)
		App.ActiveDocument.getObject(cTool).Placement = App.Placement(App.Vector(0, 16, 16),App.Rotation(App.Vector(0,0,1),0))
		nFuse += 1
		cFuse = "Fuse" + str(nFuse).zfill(5)
		App.activeDocument().addObject("Part::Fuse",cFuse)
		App.activeDocument().getObject(cFuse).Base = App.activeDocument().getObject(cBase)
		App.activeDocument().getObject(cFuse).Tool = App.activeDocument().getObject(cTool)
		Gui.activeDocument().hide(cBase)
		Gui.activeDocument().hide(cTool)
		Gui.ActiveDocument.getObject(cFuse).ShapeColor=Gui.ActiveDocument.getObject(cBase).ShapeColor
		Gui.ActiveDocument.getObject(cFuse).DisplayMode=Gui.ActiveDocument.getObject(cBase).DisplayMode
		kit0000(63, 16, nLarg - 32) # -------------------------------------------------- Regua dianteira
		cBase = "Fuse" + str(nFuse).zfill(5)
		cTool = "Box" + str(nBox).zfill(5)
		App.ActiveDocument.getObject(cTool).Placement = App.Placement(App.Vector(580 - 16, 16, 700 - 63),App.Rotation(App.Vector(0,0,1),0))
		nFuse += 1
		cFuse = "Fuse" + str(nFuse).zfill(5)
		App.activeDocument().addObject("Part::Fuse",cFuse)
		App.activeDocument().getObject(cFuse).Base = App.activeDocument().getObject(cBase)
		App.activeDocument().getObject(cFuse).Tool = App.activeDocument().getObject(cTool)
		Gui.activeDocument().hide(cBase)
		Gui.activeDocument().hide(cTool)
		Gui.ActiveDocument.getObject(cFuse).ShapeColor=Gui.ActiveDocument.getObject(cBase).ShapeColor
		Gui.ActiveDocument.getObject(cFuse).DisplayMode=Gui.ActiveDocument.getObject(cBase).DisplayMode


def kit0104(nLarg): # Movel Base Forno
	if nLarg == 600:
		global nFuse
		kit0001(700, 580)	# ------------------------------------------------ Ilharga esq.
		cBase = "Cut" + str(nCut).zfill(5)
		App.ActiveDocument.recompute()
		Gui.activeDocument().activeView().viewAxonometric()
		Gui.SendMsgToActiveView("ViewFit")
		kit0005(545, nLarg - 32)	# ------------------------------------------------ Base
		cTool = "Cut" + str(nCut).zfill(5)
		App.ActiveDocument.getObject(cTool).Placement = App.Placement(App.Vector(35, 16, 0),App.Rotation(App.Vector(0,0,1),0))
		nFuse += 1
		cFuse = "Fuse" + str(nFuse).zfill(5)
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
		kit0002(700, 580)	# ------------------------------------------------ Ilharga dir.
		cBase = "Fuse" + str(nFuse).zfill(5)
		cTool = "Cut" + str(nCut).zfill(5)
		App.ActiveDocument.getObject(cTool).Placement = App.Placement(App.Vector(0, nLarg - 16, 0),App.Rotation(App.Vector(0,0,1),0))
		nFuse += 1
		cFuse = "Fuse" + str(nFuse).zfill(5)
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
		cBase = "Fuse" + str(nFuse).zfill(5)
		cTool = "Box" + str(nBox).zfill(5)
		App.ActiveDocument.getObject(cTool).Placement = App.Placement(App.Vector(59, 16, 16),App.Rotation(App.Vector(0,0,1),0))
		nFuse += 1
		cFuse = "Fuse" + str(nFuse).zfill(5)
		App.activeDocument().addObject("Part::Fuse",cFuse)
		App.activeDocument().getObject(cFuse).Base = App.activeDocument().getObject(cBase)
		App.activeDocument().getObject(cFuse).Tool = App.activeDocument().getObject(cTool)
		Gui.activeDocument().hide(cBase)
		Gui.activeDocument().hide(cTool)
		Gui.ActiveDocument.getObject(cFuse).ShapeColor=Gui.ActiveDocument.getObject(cBase).ShapeColor
		Gui.ActiveDocument.getObject(cFuse).DisplayMode=Gui.ActiveDocument.getObject(cBase).DisplayMode
		kit0000(65, 521) # -------------------------------------------------- Regua p/Prateleira dir.
		cBase = "Fuse" + str(nFuse).zfill(5)
		cTool = "Box" + str(nBox).zfill(5)
		App.ActiveDocument.getObject(cTool).Placement = App.Placement(App.Vector(59, 568, 16),App.Rotation(App.Vector(0,0,1),0))
		nFuse += 1
		cFuse = "Fuse" + str(nFuse).zfill(5)
		App.activeDocument().addObject("Part::Fuse",cFuse)
		App.activeDocument().getObject(cFuse).Base = App.activeDocument().getObject(cBase)
		App.activeDocument().getObject(cFuse).Tool = App.activeDocument().getObject(cTool)
		Gui.activeDocument().hide(cBase)
		Gui.activeDocument().hide(cTool)
		Gui.ActiveDocument.getObject(cFuse).ShapeColor=Gui.ActiveDocument.getObject(cBase).ShapeColor
		Gui.ActiveDocument.getObject(cFuse).DisplayMode=Gui.ActiveDocument.getObject(cBase).DisplayMode
		kit0006(521, nLarg - 32) # -------------------------------------------------- Prateleira
		print cBase, str(nFuse).zfill(5)
		cBase = "Fuse" + str(nFuse).zfill(5)
		cTool = "Box" + str(nBox).zfill(5)
		App.ActiveDocument.getObject(cTool).Placement = App.Placement(App.Vector(59, 16, 81),App.Rotation(App.Vector(0,0,1),0))
		nFuse += 1
		cFuse = "Fuse" + str(nFuse).zfill(5)
		App.activeDocument().addObject("Part::Fuse",cFuse)
		App.activeDocument().getObject(cFuse).Base = App.activeDocument().getObject(cBase)
		App.activeDocument().getObject(cFuse).Tool = App.activeDocument().getObject(cTool)
		Gui.activeDocument().hide(cBase)
		Gui.activeDocument().hide(cTool)
		Gui.ActiveDocument.getObject(cFuse).ShapeColor=Gui.ActiveDocument.getObject(cBase).ShapeColor
		Gui.ActiveDocument.getObject(cFuse).DisplayMode=Gui.ActiveDocument.getObject(cBase).DisplayMode
		kit0000(90, 16, nLarg - 32) # -------------------------------------------------- Regua trazeira
		cBase = "Fuse" + str(nFuse).zfill(5)
		cTool = "Box" + str(nBox).zfill(5)
		App.ActiveDocument.getObject(cTool).Placement = App.Placement(App.Vector(0, 16, 700 - 90),App.Rotation(App.Vector(0,0,1),0))
		nFuse += 1
		cFuse = "Fuse" + str(nFuse).zfill(5)
		App.activeDocument().addObject("Part::Fuse",cFuse)
		App.activeDocument().getObject(cFuse).Base = App.activeDocument().getObject(cBase)
		App.activeDocument().getObject(cFuse).Tool = App.activeDocument().getObject(cTool)
		Gui.activeDocument().hide(cBase)
		Gui.activeDocument().hide(cTool)
		Gui.ActiveDocument.getObject(cFuse).ShapeColor=Gui.ActiveDocument.getObject(cBase).ShapeColor
		Gui.ActiveDocument.getObject(cFuse).DisplayMode=Gui.ActiveDocument.getObject(cBase).DisplayMode
		kit0000(19, 38, nLarg - 32) # -------------------------------------------------- Regua dianteira
		cBase = "Fuse" + str(nFuse).zfill(5)
		cTool = "Box" + str(nBox).zfill(5)
		App.ActiveDocument.getObject(cTool).Placement = App.Placement(App.Vector(580 - 38, 16, 700 - 19),App.Rotation(App.Vector(0,0,1),0))
		nFuse += 1
		cFuse = "Fuse" + str(nFuse).zfill(5)
		App.activeDocument().addObject("Part::Fuse",cFuse)
		App.activeDocument().getObject(cFuse).Base = App.activeDocument().getObject(cBase)
		App.activeDocument().getObject(cFuse).Tool = App.activeDocument().getObject(cTool)
		Gui.activeDocument().hide(cBase)
		Gui.activeDocument().hide(cTool)
		Gui.ActiveDocument.getObject(cFuse).ShapeColor=Gui.ActiveDocument.getObject(cBase).ShapeColor
		Gui.ActiveDocument.getObject(cFuse).DisplayMode=Gui.ActiveDocument.getObject(cBase).DisplayMode


nAgl = 16
nBox = 0
nCylinder = 0
nCut = 0
nFuse = 0

#kit0100(200) # base (interno) a chamar por outros modulos
#kit0101(600) # c/prateleira
#kit0102(500) # gavetas
#kit0103(1200) # LL
kit0001(700,580)


App.ActiveDocument.recompute()
Gui.activeDocument().activeView().viewAxonometric()
Gui.SendMsgToActiveView("ViewFit")





