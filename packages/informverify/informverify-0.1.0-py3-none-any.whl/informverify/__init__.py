import argparse
import re, os ,sys, json
import pythologist

def entry_point():
    args = do_inputs()
    path = os.path.abspath(args.INFORM_ANALYSIS)
    panels = json.loads(open(args.panel_source,'rt').read())
    if args.panel_name not in panels: raise ValueError("Error you selected a panel name not included in the panel source")
    if args.panel_version not in panels[args.panel_name]: raise ValueError("Error you selected a panel version not defined for the panel name in your panel source")
    panel = panels[args.panel_name][args.panel_version]
    sys.stderr.write("Using panel: "+str(json.dumps(panel,indent=4))+"\n")

    sys.stderr.write("\nStarting Test\n\n")

    errors = []

    #####
    test = "1. The INFORM_ANALYSIS folder should only contain directories"
    sys.stderr.write(test+"\n")
    fnames = [os.path.join(path,x) for x in os.listdir(path) if x != '.DS_Store']
    for fname in fnames:
        if not os.path.isdir(fname): 
            msg = name+" is not a directory"
            errors.append((test,msg))
    #####
    test = "2. The INFORM_ANALYSIS folder contains a GIMP directory."
    sys.stderr.write(test+"\n")
    prospective = os.path.join(path,'GIMP')
    if not os.path.isdir(prospective): 
        msg = "no gimp folder "+prospective
        errors.append((test,msg))

    #####
    test = "3. The other INFORM_ANALYSIS folders are InForm projects"
    sys.stderr.write(test+"\n")
    projects = [x for x in fnames if x != prospective]
    # Get our sample and frame components of names
    frames = dict()
    for project in projects:
        frames[project] = []
        fnames = [x for x in os.listdir(project) if x.endswith('_cell_seg_data.txt')]
        for fname in fnames:
            prefix = None
            frame = None
            m = re.match('(.*)_(\[\d+,\d+\])_cell_seg_data.txt',fname)
            if m:
                prefix = m.group(1)
                frame = m.group(2)
                frames[project].append({'prefix':prefix,'frame':frame})
                continue
            m = re.match('(.*)_(\d+)_cell_seg_data.txt',fname)
            if m:
                prefix = m.group(1)
                frame = m.group(2)
                frames[project].append({'prefix':prefix,'frame':frame})
                continue
            msg = "the filename does not fit expected naming conventions "+fname
            errors.append((test,msg))  
    if len(projects) == 0: 
        msg = "No project folders found"
        errors.append((test,msg))
    pyth = dict()
    for project in projects:
        try:
            p = pythologist.read_inForm(project,sample_index=1)
        except:
            msg = project+" failed to be read in "+project+" as an InForm project."
            errors.append((test,msg))
        pyth[project] = p

    ####
    test = "4. All frames should be present in each project"
    sys.stderr.write(test+"\n")
    projects = list(frames.keys())
    frame_names = set([x['frame'] for x in frames[projects[0]]])
    for project in projects:
        newset = set([x['frame'] for x in frames[project]])
        if frame_names != newset:
            msg = "projects do not contain the same ROIs according to the file names present"
            errors.append((test,msg))

    ####
    test = "5. All phenotypes should be defined in the panel."
    sys.stderr.write(test+"\n")
    for project in pyth:
        p = pyth[project]
        for phenotype in p.phenotypes:
            if phenotype not in panel["phenotypes"]: 
                msg = "Saw phenotype "+phenotype+" in "+project+" that is not in the panel definition"
                errors.append((test,msg))

    ####
    test = "6. All of the panel's scored stains should be covered in the project files."
    sys.stderr.write(test+"\n")
    stains = set([x['stain'] for x in panel["thresholds"]])
    for project in pyth:
        p = pyth[project]
        for stain in p.scored_stains:
            if stain in stains: stains.remove(stain)
    if len(stains) > 0:
        msg = "The following scored stains expected from the panel are not represented in the InForm projects '"+"; ".join(list(sorted(stains)))+"'\n"
        errors.append((test,msg))

    ####
    test = "7. The project folders should not contain GIMP images or GIMP created tif images"
    sys.stderr.write(test+"\n")
    for project in projects:
        xcfs = [x for x in os.listdir(project) if x.endswith('.xcf')]
        if len(xcfs) > 0:
            msg = "There are gimp files "+str(xcfs)+" present in the project directory.  If GIMP files are necessary they should be in the "
            errors.append((test,msg))
        tiffs = [x for x in os.listdir(project) if x.endswith('.tiff')]
        if len(tiffs) > 0:
            msg = "Unexpected image file(s) present in project folder "+tiffs
            errors.append((test,msg))
        tiffs = [x for x in os.listdir(project) if re.search('tumor.*tif+$',x,re.IGNORECASE) ]
        if len(tiffs) > 0:
            msg = "Unexpected image file(s) present in project folder "+tiffs
            errors.append((test,msg))
        tiffs = [x for x in os.listdir(project) if re.search('invasive_margin.*tif+$',x,re.IGNORECASE) ]
        if len(tiffs) > 0:
            msg = "Unexpected image file(s) present in project folder "+tiffs
            errors.append((test,msg))


    test = "8. The GIMP folder must contain tumor tif files for every ROI"
    sys.stderr.write(test+"\n")
    for x in frames[list(frames.keys())[0]]:
        check = os.path.join(prospective,x['prefix']+'_'+x['frame']+'_Tumor.tif')
        if not os.path.exists(check):
            msg = "Missing tumor tif "+check
            errors.append((test,msg))

    test = "9. The GIMP folder must have properly named invasive margin files if they exist"
    sys.stderr.write(test+"\n")
    tiffs = [x for x in os.listdir(prospective) if re.search('invasive_margin.*tif+$',x,re.IGNORECASE) ]
    possible = [x['prefix']+'_'+x['frame']+'_Invasive_Margin.tif' for x in frames[list(frames.keys())[0]]]
    if len(tiffs) > 0:
        for tif in tiffs:
            if tif not in possible:
                msg = "Improperly named invasive margin "+tif
                errors.append((test,msg))


    test = "10. The projects should have the same segmentation"
    sys.stderr.write(test+"\n")
    segs = dict()
    for project in pyth:
        py = pyth[project]
        df = py[['x','y','frame']]
        #df['x'] =df['x'].astype(int)
        #df['y'] = df['y'].astype(int)
        df = df.sort_values(by=['frame','x','y'])
        df['xy'] = df.apply(lambda x: str((x['x'],x['y'])),1)
        df = df.groupby('frame').apply(lambda x: str(list(x['xy']))).to_dict()
        segs[project] = df
    # Now check
    reference = segs[list(segs.keys())[0]]
    frame_names = list(reference.keys())
    for project in segs:
        for frame in segs[project]:
            #print(frame)
            if segs[project][frame] != reference[frame]:
                msg = "Segmentation is not the same between inform projects for frame "+frame
                errors.append((test,msg))

    if len(errors) == 0:
        print("PASS")
    for error in errors:
        print(error)


def do_inputs():
    parser=argparse.ArgumentParser(description="Check assumptions on InForm inputs.",formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('INFORM_ANALYSIS',help="path of the INFORM_ANALYSIS folder for a sample")
    parser.add_argument('--panel_source',help="path to json defining panels",required=True)
    parser.add_argument('--panel_name',help="name of panel",required=True)
    parser.add_argument('--panel_version',help="version of panel",required=True)
    args = parser.parse_args()
    return args