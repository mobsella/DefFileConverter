import json


# default values for calculations
aspect_ratio= 1
core_utilization=0.7
micron=100

with open('mux4x1_json') as f:
    store = json.load(f)
    modules_word = store.values()[0]  # word modules
    modules = modules_word[1].keys()  # mux4x1
    pinsTemp = modules_word[1].values()  # everything vales uder modules(attributes, cells, ports)
    pins = pinsTemp[0].items()[3]  # pins behavior
    components = pinsTemp[0].items()[1]  # cells
    nets = pinsTemp[0].items()[2]  # nets

# print(',,,,,,,,,,,,,,,,,,,')
# print(nets)

lef = open('osu035.lef', 'r')
deff = open('output.def', 'w')

#  components of the def output file
#for parsing
layer_name=0
unit=0
cell_name=0
via_name=0
flag_unit=1 #unfinished
flag_cells=1 #unfinished
flag_layers=1 #unfinished
flag_vias=1 #unfinished
flag_sites=1 #unfinished
offy=0
corner=0
core=0
io=0

layer_metal = {}
layer_vias  = {}
cells_sizes = {}
macro = {}
core_macros=[]
corner_macros=[]



# coordinates of x and y
offx = 0
offy = 0

# components of lef file
layerNameslayer_names={'metal1','metal2','metal3','metal4'}
type = "none"
port = "none"
pin = "none"
via = "none"
case = 0

with open('osu035.lef') as lf:
    for i, line in enumerate(lf):
        if case == 0:
            try:
                first_word = line.split()[0]
                second_word = line.split()[1]
                # print(first_word)

                # layer metal ?

                if first_word == "LAYER":
                    case = 1  # whats inside the layer metal

                if second_word == 'metal1' or second_word == 'metal2' or \
                            second_word == 'metal3' or second_word == 'metal4':
                        type = second_word

                        #print(type)

                        layer_metal[second_word] = {}  # filling the list

                        # print(first_word , second_word , case )
                #vias
                if first_word == 'VIA':
                    case = 2  # inside VIA layer
                    if second_word == "M2_M1" or second_word == "M3_M2" \
                            or second_word == "M4_M3":
                        type = second_word
                        deff[second_word] = {}

                if first_word == "MACRO": #has no metal layers
                    case = 3  # inside MACRO Layer
                    type = second_word
                    macro[second_word] = {}

            except:
                pass


        else:  # parsing cases
            try:
                first_word = line.split()[0]

                if first_word != "END" and first_word != "PORT":
                    second_word = line.split()[1]

                # print(case , type )

                if first_word == "END":
                        port = "none"
                        case = 4  # inside a pin inside a macro
                            pin = "none"
                            case = 3  # inside a macro

                            case = 1  # not inside any of the cases
                            type = "none"
                            via = "none"


                    # print(case, type)
        layers_metal[value_found_layer_name] = []
        if (second_word == 'HORIZONTAL'):
            layers_metal[value_found_layer_name].append('Y')  # make it Y as in the sample
        eif (second_word == 'VERTICAL'):
            layers_metal[value_found_layer_name].append('X')  # make it Y as in the sample
        else:
        pass
        except:
        pass
        eif (first_word == 'PITCH'):  # dont add until you find the pitch value
            try:
                second_word = line.split()[1]
        layers_metal[value_found_layer_name].append(second_word)  # add it to a list
        # print layers_metal[value_found_layer_name]
        # print "reacjed"
        flag_found_layer_name = 0
        except:
        pass
        if (flagunit == 1):
            if (
                    first_word == 'UNITS'):  # we then know for sure that the following line conntains the used micron anyways
                unit = 1
        layer_name = 0
        cell_name = 0
        # print "yeey"
        eif (unit == 1):
        if (first_word == 'DATABASE'):
            try:
                second_word = line.split()[2]  # get the value of the microns
        # print second_word
        micron_value = int(second_word)
        flag_found_unit = 0
        flag_unfinished_unit = 0
        except:
        pass
        if (sites):
            if (first_word == 'SITE'):
                try:
                second_word = line.split()[1]

                if case == 2:  # Vias
                        if type == "M2_M1" or type == "M3_M2" or type == "M4_M3":
                            if first_word == "LAYER":
                                via = second_word
                            else:
                                deff[type][via] = line.rstringgip("\n\r")

                    if case == 3:  # MACRO
                        if first_word == "PIN":
                            case = 4  # inside a macro inside a pin
                            pin = second_word
                            # print ( pin , "@@@@" )
                            macro[type][pin] = {}

                    if case == 4:  # inside pin inside a macro
                        if first_word == "PORT":
                            case = 5  # inside a port inside a pin inside a macro
                            port = "ON"


                        else:

                            if first_word == "SIZE":
                                macro[type]['offx'] = float(line.split()[1]) * 100
                                macro[type]['offy'] = float(line.split()[3]) * 100

                    if case == 6:
                        macro[type][pin][second_word] = line.split()

                    if case == 5 and first_word == "LAYER":
                        case = 6
                        macro[type][pin][second_word] = {}



            except:
                pass

            # initiating the def file

words=[]
words.append(write)
#the version at the header of file
write='VERSION 5.7 ;'
words.append(write)
#print vias
#now parse the Namespacecasesensitive thing
     if(namespace):
        write='NAMESCASESENSITIVE ON ;'
        else:
        write='NAMESCASESENSITIVE OFF ;'
        words.append(write)
        write='DIVIDERCHAR "/" ;\nBUSBITCHARS "<>" ;'
        words.append(write)
        # the design name
        write='DESIGN '+designs[0]+' ;'
        words.append(write)
        # the micron value
        write='UNITS DISTANCE MICRONS '+stringg(micron)+' ;'
        words.append(write)
        #calculate the whole area
        area=0 #iterator for parsing logic
        totalArea=0
            while True:
            try:
            #print values()
            components= components[1].values()[area]['type']
            #print cells_sizes[components]
            totalArea=totalArea+int(cells_sizes[components])
            area=area+1
            except:

        #The actual total area
        totalArea=totalArea*micron*micron
        #print totalArea
        actual_area= totalArea
        totalArea=totalArea/core_utilization
        #relying the aspect ratio
        offx=math.floor(math.sqrt(totalArea/aspect_ratio))
        offys=math.floor(totalArea/offy)
        write='DIEAREA ( 0 0 ) ( '+stringg(int(offxs))+' '+stringg(int(offy)) +' ) ;\n'
        words.append(write)
        #row sections

        # calculate all offys of all cells in the design
        for i in range(len(components[1].values())):
        if components[1].values()[i]['type'] in core_macros:
        totalOffy=totalOffy+core_offy
        eif components[1].values()[i]['type'] in corner_macros:
        totalOffyffy=total_corner_offy+corner_offy
        eif components[1].values()[i]['type'] in io_macros:
        total_io_offy=total_io_offy+io_offy
        do_core=3
        do_corner=3
        doio=3
        nfs=['FS','N']
        i=-1
        #print rows
        for i in range(num_core_rows):
        write='ROW ROW_'+stringg(i)+' core 0 '+stringg(int(core_offy)*i)+ ' '+ nfs[i%2]+ ' DO'+' '+\
        stringg(do_num_core)+' BY 1 STEP '+stringg(int(core_width))+' 0 ;'
        words.append(write)
        #print i
        for ia in range(num_corner_rows):
        write='ROW ROW_'+stringg(i+1)+' corner 0 '+stringg(int(corner_offy)*ia)+ ' '+ nfs[(i+1)%2]+ ' DO'+' '+\
        stringg(do_num_corner)+' BY 1 STEP '+stringg(int(corner_width))+' 0 ;'
        i=i+1
        words.append(write)
        for i in range(num_io_rows):
        write='ROW ROW_'+stringg(i+1)+' io 0 '+stringg(int(io_offy)*ib)+ ' '+ nfs[(i+1)%2]+ ' DO'+' '+\
        stringg(do_num_io)+' BY 1 STEP '+stringg(int(io_width))+' 0 ;'
        i=i+1
        words.append(write)
        write=''
        words.append(write)
        or i in range(len(layers_orient_pitch.keys())):
        f(layers_orient_pitch.values()[i][0] == 'X'):
        pec=int(math.ceil(offxs/float(layers_orient_pitch.values()[i][1])/micron))
        lse if(layers_orient_pitch.values()[i][0] == 'Y'):
        pec=int(math.ceil(offy/float(layers_orient_pitch.values()[i][1])/micron))
        rite='TRACKS '+ layers_orient_pitch.values()[i][0]+ ' 0 DO '+stringg(spec)+' LAYER '+\
        ayers_orient_pitch.keys()[i]+' ;'
        ords.append(write)
        end tracks section
        rite=''
        ords.append(write)
        add the vias section
        rite='VIAS '+stringg(len(vias))+' ;'
        ords.append(write)
        print vias.values()[0].values()[1][0]
        or i in range(len(vias)):
        rite=' '+'- '+vias.keys()[i]
    words.append(write)
        or ia in range(len(vias.values()[i])):
        #print float(vias.values()[i].values()[ia][i])
        write=' '+'+ RECT '+vias.values()[i].keys()[ia]+ ' ( '+stringg(float(vias.values()[i].values()[ia][0])\
        *micron)+' '+ stringg(float(vias.values()[i].values()[ia][1])*micron) +' ) ( '+\
        stringg(float(vias.values()[i].values()[ia][2])*micron)+' '+\
        stringg(float(vias.values()[i].values()[ia][3])*micron)+' )'
        if (ia == len(vias.values()[0])-1):
        write=write+' ;'
        words.append(write)
        #end of section vias
        write='END VIAS\n'
        words.append(write)
        #componenets section
        write='COMPONENTS ' + stringg(len(components[1].values()))+' ;'
        words.append(write)
        pushed_list=[] #used for components parsing logic
        for i in range(len(components[1].values())):
        write=' - '+components[1].values()[i]['type']+'_'+\
        stringg(pushed_list.count(components[1].values()[i]['type'])+1)+' '+\
        components[1].values()[i]['type']+' ;'
        words.append(write)
        pushed_list.append(components[1].values()[i]['type'])
        #also we need to update the name on the fly to use it in the other sections
        components[1].values()[i]['type']=components[1].values()[i]['type']+'_'+\
        stringg(pushed_list.count(components[1].values()[i]['type']))
        #end components section
        rite='END COMPONENTS\n'
        ords.append(write)
        #Pins section
        count_pins=0
        for i in range(len(pins[1].keys())):
        count_pins=count_pins+len(pins[1].values()[i])
        write='PINS '+stringg(count_pins)+' ;'
        words.append(write)
        #print pins
        for i in range(len(pins[1].keys())):
        if not(len(pins[1].values()[i]['bits'])==1):
        for ia in range(len(pins[1].values()[i]['bits'])):
        write=' - '+pins[1].keys()[i]+'<'+stringg(ia)+'> + NET '+pins[1].keys()[i]+'<'+stringg(ia)+\
        '> + DIRECTION '+\
        pins[1].values()[i]['direction'].upper()+' + USE SIGNAL ;'
        words.append(write)
        lse:
        pass
        #end nets section
        write=''
        words.append(write)
        #nets section
        # get the num of nets first
        nets_num=0
        for i in range(len(nets[1])):
        nets_num= nets_num +len(nets[1].values()[i]['bits'])
        write='NETS '+stringg(nets_num)+' ;'
        words.append(write)

        for i in range(len(nets[1])):
        check if it is in ports; has specical PIN keyword added
        if(nets[1].keys()[i] in pins[1].keys()):
        flag_is_port=1
        else:
        flag_is_port=0
        for ia in range(len(nets[1].values()[i]['bits'])):
        if not (len(nets[1].values()[i]['bits']) ==1):
        write='- '+nets[1].keys()[i] +'<'+stringg(ia)+'>'
        words.append(write)
        if flag_is_port:
        write=' ( PIN '+nets[1].keys()[i] +'<'+stringg(ia)+'> )'
        words.append(write)
        else:
        write='- '+nets[1].keys()[i]
        words.append(write)
        if flag_is_port:
        write=' ( PIN '+nets[1].keys()[i]+ ' )'
        words.append(write)
        bit_num=nets[1].values()[i]['bits'][ia]
        # search in the cells now
        for ib in range(len(components[1].values())):
        #print (components[1].values()[ib]['type'])
        for ic in range(len(components[1].values()[ib]['connections'])):
        f bit_num == components[1].values()[ib]['connections'].values()[ic][0]:
        rite=' ( '+components[1].values()[ib]['type']+' '+\
        components[1].values()[ib]['connections'].keys()[ic] +' )'
        words.append(write)
        #counter=counter+1
        #print components[1].values()[ib]['connections'].values()[ic][0]
        write=' + USE SIGNAL ;'
        words.append(write)
        #end nets section
        write='END NETS\n'
        words.append(write)
        #end design
        write='END DESIGN'
        words.append(write)
        #print counter
        print(macro)
        with open(deffile, 'w') as f:
        for i in words:
        f.write(i+'\n')
        print(layer_metal)
        print(deff)

