import glob
import os
import config
import lifx
from time import sleep, time
from tkinter import *
import pyttsx3
import json

engine = pyttsx3.init()


# lights
def whiteBright():
    try:
        lifx.whiteBright()
    except:
        print("Failed LIFX")

def whiteDim():

    try:
        lifx.whiteDim()
    except:
        print("Failed LIFX")
    
def orange():

    try:
        lifx.orange()
    except:
        print("Failed LIFX")
        
    
def flashGreen():

   lifx.flashGreen(0.5)
   sleep(0.5)
   lifx.flashGreen(0.5)
   sleep(0.5)
   lifx.flashGreen(0.5)
    
def flashRed():

   lifx.flashRed(0.5)
   sleep(0.5)
   lifx.flashRed(0.5)
   sleep(0.5)
   lifx.flashRed(0.5)

    
def flashYellow():

   lifx.flashYellow(0.5)
   sleep(0.5)
   lifx.flashYellow(0.5)
   sleep(0.5)
   lifx.flashYellow(0.5)
    

# start as dim white
lifx.default()

sleep(5)

def get_log():
    # get latest log
    list_of_files = glob.glob(config.logLocation)
    try:
        latest_file = max(list_of_files, key=os.path.getctime)
    except:
        print("Please add your Elite Dangerous log file location to the config.py file before running")

    return latest_file
        

# define events
underAttack = '"event":"UnderAttack", "Target":"You"'
hullDamage = '"event":"HullDamage"'
heatDamage = '"event":"HeatDamage"'
heatWarning = '"event":"HeatWarning"'
shieldOff = '"ShieldsUp":false'
shieldOn = '"ShieldsUp":true'

kill = '"event":"PVPKill"'

supercruiseEnter = '"event":"StartJump", "JumpType":"Supercruise"'
supercruiseExit = '"event":"SupercruiseExit"'
hyper_space = '"event":"StartJump", "JumpType":"Hyperspace"'
hyper_space_exit = '"MusicTrack":"DestinationFromHyperspace"'

fuel = '"event":"ReservoirReplenished",'
refuel = '"event":"RefuelAll"'
repair = '"event":"RepairAll"'
stock = 'fgdsgrerrrrrrrrrgbfxvbfdbndfnfbfbd'
scanned = '"event":"Scanned"'

system_map = '"MusicTrack":"SystemMap"'
galaxy_map = '"MusicTrack":"GalaxyMap"'
scanner = 'SystemAndSurfaceScanner'
dscan  = '"event":"FSSDiscoveryScan"'
defalut = '"MusicTrack":"NoTrack"'
defalut2 = ' "MusicTrack":"Exploration"'
super_cruise_music =' "MusicTrack":"Supercruise"'

dockGranted = '"event":"DockingGranted"'
dockingMusic = '"MusicTrack":"DockingComputer"'
dockedMusic = '"MusicTrack":"Starport"'

shutdown = '"event":"Shutdown"'
menu =  '"event":"Music", "MusicTrack":"MainMenu"'
discovered =  '"event":"FSSSignalDiscovered"'
fsd_target = '"event":"FSDTarget"'
collected = ' "event":"MaterialCollected"'

mission_accepted = '"event":"MissionAccepted"'
dead = '"event":"Died"'
ressurect = '"event":"Resurrect"'

buy_drones = '"event":"BuyDrones"'

cargo =  '"event":"CollectCargo"'
cargo2 =  '"event":"Cargo"'

target =  '"event":"ShipTargeted"'


last_log_update = time()
last_alert = 0

log_update_seconds = 60
alert_update_seconds = 120

time_running = 10**100 # BIG number

latest_file = get_log()
with open(latest_file, 'r') as currentLog:
    while True:
        sleep(0.1)
        # Refresh log file
        if time() - last_log_update > log_update_seconds:
            new_file = get_log()
            if new_file != latest_file:
                currentLog = open(latest_file, 'r')
            last_log_update = time()

        # Read lines
        lines = currentLog.read().splitlines()
        
        if len(lines) != 0:
            # Last line of log (most recent event)
            lastLine = str(lines[-1])

            # Ingnore text events for now
            if '"event":"ReceiveText"' in lastLine:
                continue

            print(lastLine)

            # Ship targeted / interdiction
            if target in lastLine:
                data = json.loads(lastLine)
                engine.say("Target")
                engine.runAndWait()
                if 'Ship_Localised' in data:
                    engine.say(data['Ship_Localised'])
                else:
                     engine.say(data['Ship'])
                engine.runAndWait()
                engine.say(f"Scan stage {data['ScanStage']}")
                engine.runAndWait()
                if 'LegalStatus' in data:
                    engine.say(f"Status {data['LegalStatus']}")
                    engine.runAndWait()

            # Shutdown
            if shutdown in lastLine or menu in lastLine:
                if time_running < time():
                    print(time_running)
                    print(time())
                    lifx.off()
                    time_running = time()
                else:
                    print('Ignore last shutdown')

            # under attack
            elif underAttack in lastLine:
                if time() - last_alert > alert_update_seconds:
                    last_alert = time()
                    flashYellow()
                else:
                    print('No alert yet')

            elif shieldOff in lastLine:
                lifx.yellow()
            elif dockedMusic in lastLine: 
                lifx.docked_blue()
            elif shieldOn in lastLine:
                lifx.pulse_green()
                sleep(0.5)
                lifx.default()
            elif dockGranted in lastLine or kill in lastLine:
                flashGreen()
            elif hyper_space in lastLine:
                lifx.blue()
            elif hyper_space_exit in lastLine:
                lifx.blue()
                sleep(0.3)
                lifx.default()  
            elif heatWarning in lastLine:
                lifx.orange()
            elif heatDamage in lastLine or dead in lastLine:
                lifx.red()
            elif hullDamage in lastLine or cargo in lastLine:
                flashRed()
            elif dscan in lastLine or supercruiseEnter in lastLine:
                lifx.pulse_blue()
            elif refuel in lastLine or repair in lastLine or stock in lastLine or collected in lastLine or mission_accepted in lastLine or buy_drones in lastLine:
                lifx.pulse_green()
            elif discovered in lastLine:
                lifx.pulse_red() 
            elif system_map in lastLine or scanner in lastLine or galaxy_map in lastLine:
                lifx.dark()
            elif defalut in lastLine or defalut2 in lastLine:
                lifx.default()
            elif dockingMusic in lastLine:
                lifx.green()
            elif super_cruise_music in lastLine:
                lifx.orange_dark()
            elif ressurect in lastLine:
                lifx.whiteBright
                sleep(0.75)
            else:
                print('no match')


