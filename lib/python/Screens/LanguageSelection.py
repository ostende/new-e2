from Screens.Screen import Screen
<<<<<<< HEAD
from Screens.MessageBox import MessageBox
=======
>>>>>>> dev/Dev
from Components.ActionMap import ActionMap
from Components.Language import language
from Components.config import config
from Components.Sources.List import List
from Components.Label import Label
from Components.Sources.StaticText import StaticText
from Components.Pixmap import Pixmap
from Screens.InfoBar import InfoBar
<<<<<<< HEAD
from Components.Language_cache import LANG_TEXT
from enigma import eTimer

from Screens.Rc import Rc

from Tools.Directories import resolveFilename, SCOPE_ACTIVE_SKIN
from Tools.LoadPixmap import LoadPixmap
import gettext

inWizzard = False
=======
from Screens.Rc import Rc
from Tools.Directories import resolveFilename, SCOPE_ACTIVE_SKIN
from Tools.LoadPixmap import LoadPixmap

>>>>>>> dev/Dev

def LanguageEntryComponent(file, name, index):
	png = LoadPixmap(resolveFilename(SCOPE_ACTIVE_SKIN, "countries/" + index + ".png"))
	if png is None:
		png = LoadPixmap(resolveFilename(SCOPE_ACTIVE_SKIN, "countries/" + file + ".png"))
		if png is None:
			png = LoadPixmap(resolveFilename(SCOPE_ACTIVE_SKIN, "countries/missing.png"))
	res = (index, name, png)
	return res

<<<<<<< HEAD
def _cached(x):
	return LANG_TEXT.get(config.osd.language.value, {}).get(x, "")

=======
>>>>>>> dev/Dev
class LanguageSelection(Screen):
	def __init__(self, session, menu_path=""):
		Screen.__init__(self, session)
		screentitle = _("Language")
		if config.usage.show_menupath.value == 'large':
			menu_path += screentitle
			title = menu_path
			self["menu_path_compressed"] = StaticText("")
		elif config.usage.show_menupath.value == 'small':
			title = screentitle
			self["menu_path_compressed"] = StaticText(menu_path + " >" if not menu_path.endswith(' / ') else menu_path[:-3] + " >" or "")
		else:
			title = screentitle
			self["menu_path_compressed"] = StaticText("")
		Screen.setTitle(self, title)

<<<<<<< HEAD
		language.InitLang()
		self.oldActiveLanguage = language.getActiveLanguage()
		self.catalog = language.getActiveCatalog()

		self.list = []
# 		self["flag"] = Pixmap()
		self["summarylangname"] = StaticText()
		self["summarylangsel"] = StaticText()
		self["languages"] = List(self.list)
		self["languages"].onSelectionChanged.append(self.changed)
=======
		self.oldActiveLanguage = language.getActiveLanguage()

		self.list = []
		self["summarylangname"] = StaticText()
		self["languages"] = List(self.list)
>>>>>>> dev/Dev

		self.updateList()
		self.onLayoutFinish.append(self.selectActiveLanguage)

		self["key_red"] = Label(_("Cancel"))
		self["key_green"] = Label(_("Save"))
<<<<<<< HEAD
		self["key_yellow"] = Label(_("Update Cache"))
		self["key_blue"] = Label(_("Delete Language"))

		self["actions"] = ActionMap(["SetupActions", "ColorActions"],
=======

		self["actions"] = ActionMap(["OkCancelActions", "ColorActions"],
>>>>>>> dev/Dev
		{
			"ok": self.save,
			"cancel": self.cancel,
			"red": self.cancel,
			"green": self.save,
<<<<<<< HEAD
			"yellow": self.updateCache,
			"blue": self.delLang,
		}, -1)

	def updateCache(self):
		print"updateCache"
		self["languages"].setList([('update cache','Updating cache, please wait...',None)])
		self.updateTimer = eTimer()
		self.updateTimer.callback.append(self.startupdateCache)
		self.updateTimer.start(100)

	def startupdateCache(self):
		self.updateTimer.stop()
		language.updateLanguageCache()
		self["languages"].setList(self.list)
		self.selectActiveLanguage()
		
	def selectActiveLanguage(self):
		activeLanguage = language.getActiveLanguage()
		pos = 0
		for x in self.list:
			if x[0] == activeLanguage:
				self["languages"].index = pos
				break
			pos += 1

	def save(self):
		self.run()
		global inWizzard
		if inWizzard:
			inWizzard = False
			self.session.openWithCallback(self.deletelanguagesCB, MessageBox, _("Do you want to delete all other languages?"), default = False)
		else:
			self.close(self.oldActiveLanguage != config.osd.language.value)

	def deletelanguagesCB(self, anwser):
		if anwser:
			language.delLanguage()
		self.close()

	def cancel(self):
		language.activateLanguage(self.oldActiveLanguage)
		config.osd.language.setValue(self.oldActiveLanguage)
		config.osd.language.save()
		self.close()

	def delLang(self):
		curlang = config.osd.language.value
		lang = curlang
		languageList = language.getLanguageListSelection()
		for t in languageList:
			if curlang == t[0]:
				lang = t[1]
				break
		self.session.openWithCallback(self.delLangCB, MessageBox, _("Do you want to delete all other languages?") + _(" Except %s") %(lang), default = False)

	def delLangCB(self, anwser):
		if anwser:
			language.delLanguage()
			language.activateLanguage(self.oldActiveLanguage)
			self.updateList()
			self.selectActiveLanguage()

	def run(self, justlocal = False):
		print "updating language..."
		lang = self["languages"].getCurrent()[0]

		if lang == 'update cache':
			self.setTitle("Updating cache")
			self["summarylangname"].setText("Updating cache")
			return

		if lang != config.osd.language.value:
			config.osd.language.setValue(lang)
			config.osd.language.save()

		self.setTitle(_cached("T2"))
		self["summarylangname"].setText(_cached("T2"))
		self["summarylangsel"].setText(self["languages"].getCurrent()[1])
		self["key_red"].setText(_cached("T3"))
		self["key_green"].setText(_cached("T4"))
# 		index = self["languages"].getCurrent()[2]
# 		print 'INDEX:',index
# 		self["flag"].instance.setPixmap(self["languages"].getCurrent()[2])

		if justlocal:
			return

		language.activateLanguage(lang)
		config.misc.languageselected.value = 0
		config.misc.languageselected.save()
		print "ok"
=======
		}, -1)

	def selectActiveLanguage(self):
		self.setTitle(self.title)
		pos = 0
		for pos, x in enumerate(self.list):
			if x[0] == self.oldActiveLanguage:
				self["languages"].index = pos
				break

	def save(self):
		self.commit(self.run())
		if InfoBar.instance and self.oldActiveLanguage != config.osd.language.value:
			self.close(True)
		else:
			self.close()

	def cancel(self):
		language.activateLanguage(self.oldActiveLanguage)
		self.close()

	def run(self):
		print "[LanguageSelection] updating language..."
		lang = self["languages"].getCurrent()[0]
		if lang != config.osd.language.value:
			config.osd.language.setValue(lang)
			config.osd.language.save()
		return lang
>>>>>>> dev/Dev

	def commit(self, lang):
		print "[LanguageSelection] commit language"
		language.activateLanguage(lang)
		config.misc.languageselected.value = 0
<<<<<<< HEAD
		config.misc.languageselected.save()		
		
=======
		config.misc.languageselected.save()

>>>>>>> dev/Dev
	def updateList(self):
		languageList = language.getLanguageList()
		if not languageList: # no language available => display only english
			list = [ LanguageEntryComponent("en", "English (UK)", "en_GB") ]
		else:
			list = [ LanguageEntryComponent(file = x[1][2].lower(), name = x[1][0], index = x[0]) for x in languageList]
		self.list = list
		self["languages"].list = list

<<<<<<< HEAD
	def changed(self):
		self.run(justlocal = True)

=======
>>>>>>> dev/Dev
class LanguageWizard(LanguageSelection, Rc):
	def __init__(self, session):
		LanguageSelection.__init__(self, session)
		Rc.__init__(self)
<<<<<<< HEAD
		global inWizzard
		inWizzard = True
		self.onLayoutFinish.append(self.selectKeys)

=======
		self.onLayoutFinish.append(self.selectKeys)
>>>>>>> dev/Dev
		self["wizard"] = Pixmap()
		self["summarytext"] = StaticText()
		self["text"] = Label()
		self.setText()

	def selectKeys(self):
		self.clearSelectedKeys()
		self.selectKey("UP")
		self.selectKey("DOWN")

<<<<<<< HEAD
	def changed(self):
		self.run(justlocal = True)
		self.setText()

	def setText(self):
		self["text"].setText(_cached("T1"))
		self["summarytext"].setText(_cached("T1"))
=======
	def setText(self):
		self["text"].setText(_("Please use the UP/DOWN keys to select your language. Then press the OK button to select it."))
		self["summarytext"].setText(_("Please use the UP/DOWN keys to select your language. Then press the OK button to select it."))
>>>>>>> dev/Dev

	def createSummary(self):
		return LanguageWizardSummary

class LanguageWizardSummary(Screen):
	def __init__(self, session, parent):
		Screen.__init__(self, session, parent)
