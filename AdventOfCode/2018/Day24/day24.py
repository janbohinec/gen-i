# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 20:42:22 2018

@author: Jan
"""

import numpy as np
import pandas as pd
import time
import re



## Advent of Code 2018, Day 24
day = 24


if __name__ == '__main__':
    
    t1 = time.time()
    print("***  It's Advent of Code 2018, Day {0}!  ***\n".format(day))
    print('** First part:')
    
    prod = True
    test = ''
    if not prod:
        test = 'Test'
        
    boost = 83
    print('Boost: ', boost)
      
    with open('day{0}immune{1}.txt'.format(day, test), 'r') as f:
        data_immune = [line.strip() for line in f.readlines()]
    
    with open('day{0}infections{1}.txt'.format(day, test), 'r') as f:
        data_infection = [line.strip() for line in f.readlines()]        

    magicTypes = {'cold': 0,
                   'bludgeoning': 1, 
                   'fire': 2,
                   'slashing': 3,
                   'radiation': 4
                   }

    immuneSystem = [] # units, hit points, attack, initiative, initial health, current health, weakness, immunity, attack type, effective power
    for group in data_immune:
        units, hits, attack, initiative = list(map(int, re.findall(r'\d+', group)))
        weakness = re.findall(r'weak to (\w+)', group)
        immunity = re.findall(r'immune to (\w+)', group)
        attackType = re.findall(r'(\w+) damage', group)
        immuneSystem += [['Immune', units, units, hits, attack + boost, initiative, units*hits, units*hits, [magicTypes[k] for k in weakness], [magicTypes[k] for k in immunity], magicTypes[attackType[0]], units*attack]]
        #immuneSystem += [['Immune',units, hits, attack, initiative, units*hits, units*hits, weakness, immunity, attackType[0], units*attack]]
    
    # correction, because my re knowledge sucks
    if prod:
        immuneSystem[-1][9] = [magicTypes[k] for k in ['slashing', 'bludgeoning']] # immune
    else:
        immuneSystem[0][8] = [magicTypes[k] for k in ['radiation', 'bludgeoning']] # weak
        immuneSystem[1][8] = [magicTypes[k] for k in ['slashing', 'bludgeoning']] # weak
    
    immuneSystem = pd.DataFrame(immuneSystem, columns = ['Army', 'IniUnits', 'CurUnits', 'HitPoints', 'Attack', 'Initiative', 'InitiaHealth', 'CurHealth', 'Weakness', 'Immunity', 'AttackType', 'EffPower'])
    
    infectionSystem = [] # units, hit points, attack, initiative, initial health, current health, defense weak, attack type
    for group in data_infection:
        units, hits, attack, initiative = list(map(int, re.findall(r'\d+', group)))
        weakness = re.findall(r'weak to (\w+)', group)
        immunity = re.findall(r'immune to (\w+)', group)
        attackType = re.findall(r'(\w+) damage', group)
        infectionSystem += [['Infection', units, units, hits, attack, initiative, units*hits, units*hits, [magicTypes[k] for k in weakness], [magicTypes[k] for k in immunity], magicTypes[attackType[0]], units*attack]]
        #infectionSystem += [['Infection', units, units, hits, attack, initiative, units*hits, units*hits, weakness, immunity, attackType, units*attack]]
    
    # correction, because my re knowledge sucks
    if prod:
        infectionSystem[0][9] = [magicTypes[k] for k in ['slashing', 'radiation','bludgeoning']] # immune
        infectionSystem[-3][8] = [magicTypes[k] for k in ['cold', 'slashing']] # weak
        infectionSystem[-1][8] = [magicTypes[k] for k in ['cold', 'fire']] # weak
    else:
        infectionSystem[-1][8] = [magicTypes[k] for k in ['cold', 'fire']] # weak
    infectionSystem = pd.DataFrame(infectionSystem, columns = ['Army', 'IniUnits', 'CurUnits', 'HitPoints', 'Attack', 'Initiative', 'InitiaHealth', 'CurHealth', 'Weakness', 'Immunity', 'AttackType', 'EffPower'])
    
    system = pd.concat([infectionSystem, immuneSystem])
    system.reset_index(inplace=True)
    
    #print(system) # initial state
    
    
    system['Target'] = None
    system['TargetDamage'] = None
    system['Selected'] = 0
    system['EffPower'] = system['Attack'] * system['CurUnits']
    del system['CurHealth']
    del system['InitiaHealth']
    del system['index']

    # target Selection
    infectionActiveUnits = system[(system.Army == 'Infection') & (system.CurUnits > 0)].sort_values(by=['EffPower', 'Initiative'], ascending=False)
    immuneActiveUnits = system[(system.Army == 'Immune') & (system.CurUnits > 0)].sort_values(by=['EffPower', 'Initiative'], ascending=False)
    rnd  = 0
    
    while len(infectionActiveUnits) > 0 or len(immuneActiveUnits) > 0:
    #while rnd < 1:
        # one army targeting
        for idx, unitAttacking in infectionActiveUnits.iterrows():
            maxDamage = 0
            maxEffPower = 0
            maxInitiative = -1
            for idx_, unitDefending in immuneActiveUnits.iterrows():
                #print(unitInf.AttackType, unitImmune.Weakness, unitImmune.Immunity)
                if unitDefending.Selected == 1:# Target already selected
                    #print('Target already selected')
                    damage = 0
                    continue
                if unitAttacking.AttackType in unitDefending.Weakness:
                    #print('Double damage!')
                    damage = unitAttacking.EffPower * 2
                elif unitAttacking.AttackType in unitDefending.Immunity:
                    #print('Resistance!')
                    damage = 0
                else:
                    damage = unitAttacking.EffPower
                if damage >= maxDamage:
                    if damage > maxDamage or maxEffPower < unitDefending.EffPower:
                        maxDamage = damage
                        target = idx_
                        maxEffPower = unitDefending.EffPower
                        maxInitiative = unitDefending.Initiative
                    elif maxEffPower == unitDefending.EffPower:
                        if maxInitiative < unitDefending.Initiative:
                            maxDamage = damage
                            target = idx_
                            maxEffPower = unitDefending.EffPower
                            maxInitiative = unitDefending.Initiative
                        
                #print('Infection group ', idx, 'would deal defending group ', idx_, damage, 'damage')
            if maxDamage > 0: # Attack really happens
                immuneActiveUnits.loc[target, 'Selected'] = 1
                system.loc[idx, 'Target'] = target
                system.loc[idx, 'TargetDamage'] = maxDamage / unitAttacking.EffPower
        
        # 2nd army targeting
        for idx, unitAttacking in immuneActiveUnits.iterrows():
            maxDamage = 0
            maxEffPower = 0
            maxInitiative = -1
            for idx_, unitDefending in infectionActiveUnits.iterrows():
                #print(unitInf.AttackType, unitImmune.Weakness, unitImmune.Immunity)
                if unitDefending.Selected == 1:# Target already selected
                    #print('Target already selected')
                    damage = 0
                    continue
                if unitAttacking.AttackType in unitDefending.Weakness:
                    #print('Double damage!')
                    damage = unitAttacking.EffPower * 2
                elif unitAttacking.AttackType in unitDefending.Immunity:
                    #print('Resistance!')
                    damage = 0
                else:
                    damage = unitAttacking.EffPower
                if damage >= maxDamage:
                    if damage > maxDamage or maxEffPower < unitDefending.EffPower:
                        maxDamage = damage
                        target = idx_
                        maxEffPower = unitDefending.EffPower
                        maxInitiative = unitDefending.Initiative  
                    elif maxEffPower == unitDefending.EffPower:
                        if maxInitiative < unitDefending.Initiative:
                            maxDamage = damage
                            target = idx_
                            maxEffPower = unitDefending.EffPower
                            maxInitiative = unitDefending.Initiative  
                #print('Infection group ', idx, 'would deal defending group ', idx_, damage, 'damage')
            if maxDamage > 0: # Attack really happens
                infectionActiveUnits.loc[target, 'Selected'] = 1
                system.loc[idx, 'Target'] = target
                system.loc[idx, 'TargetDamage'] = maxDamage / unitAttacking.EffPower 
        
        #print(system)
  
        # Attacking phase
        # delete cur units by the ammount of damage
        for idx, unitAttacking in system[system.Target >= 0].sort_values(by=['Initiative'],ascending=False).iterrows():
            killingUnits = (system.loc[idx, 'TargetDamage'] * system.loc[idx, 'EffPower']) // system.loc[unitAttacking.Target, 'HitPoints']
            system.loc[unitAttacking.Target, 'CurUnits'] = int(max(0, system.loc[unitAttacking.Target, 'CurUnits'] - killingUnits))
            system.loc[unitAttacking.Target, 'EffPower'] = int(max(0, system.loc[unitAttacking.Target, 'Attack'] * system.loc[unitAttacking.Target, 'CurUnits']))
            #print(unitAttacking.Army, 'group ', idx, 'attacks defending group ', unitAttacking.Target, 'killing ',killingUnits, ' units')
    
        # another round
        system['Target'] = None
        system['TargetDamage'] = None
        system['Selected'] = 0
        #system['EffPower'] = system['Attack'] * system['CurUnits']
    
        # target Selection
        infectionActiveUnits = system[(system.Army == 'Infection') & (system.CurUnits > 0)].sort_values(by=['EffPower', 'Initiative'], ascending=False)
        immuneActiveUnits = system[(system.Army == 'Immune') & (system.CurUnits > 0)].sort_values(by=['EffPower', 'Initiative'], ascending=False)
        
        rnd += 1
        if rnd % 100 == 0:
            print(rnd, len(infectionActiveUnits), len(immuneActiveUnits), infectionActiveUnits.CurUnits.sum(), immuneActiveUnits.CurUnits.sum())
        if infectionActiveUnits.CurUnits.sum() == 0 or immuneActiveUnits.CurUnits.sum() == 0:
            print('End of fight!')
            print(rnd, len(infectionActiveUnits), len(immuneActiveUnits), infectionActiveUnits.CurUnits.sum(), immuneActiveUnits.CurUnits.sum())
            break
        
        
    res = 0
    
    print('Silver star answer: \n{0}'.format(res))
    
    print('** Second part:')
    
    
   
    
    print('Golden star answer: \n{0}'.format(res))
    t2 = time.time()
    print('Program run for  {0} sec.'.format(round(t2-t1,2)))

