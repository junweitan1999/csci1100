def life_tick(grid_before_tick, grid_after_tick) :
    for row_number in range(len(grid_before_tick)):
        for column_number in range(len(grid_before_tick[0])):
            lst = []
            if row_number==len(grid_before_tick)-1:
                row_number=-1
            if column_number==len(grid_before_tick[0])-1:
                column_number=-1
            lst.append(grid_before_tick[row_number-1][column_number])
            lst.append(grid_before_tick[row_number-1][column_number-1])
            lst.append(grid_before_tick[row_number][column_number-1])
            lst.append(grid_before_tick[row_number+1][column_number])
            lst.append(grid_before_tick[row_number+1][column_number+1])
            lst.append(grid_before_tick[row_number][column_number+1])
            lst.append(grid_before_tick[row_number+1][column_number-1])
            lst.append(grid_before_tick[row_number-1][column_number+1])
            if grid_before_tick[row_number][column_number] == 1:
                live_count =0
                for i in lst:
                    if i ==1:
                        live_count+=1
                if live_count<2:
                    grid_after_tick[row_number][column_number]=0
                if live_count==2 or live_count==3:
                    grid_after_tick[row_number][column_number]=1
                if live_count>3:
                    grid_after_tick[row_number][column_number]=0
            if grid_before_tick[row_number][column_number] == 0:
                live_count =0
                for i in lst:
                    if i ==1:
                        live_count+=1
                if live_count==3:
                    grid_after_tick[row_number][column_number] = 1


def read_init(config):
    txt=open(config[0],"r")
    line=txt.readline()
    head = line
    line=txt.readlines()
    txt.close()
    count=0
    for row in line:
        line[count] = row.strip("\n")
        count+=1
    count=0
    for row in line:
        line[count] = row.split(",")
        count+=1
    for i in range (config[1]) :
        lst=[]
        for row_list in line:
            lst.append(row_list[:])
        life_tick(line, lst)
        print(line)
        print(lst)
        #txt=open("grid_{0}.out.life".format(i),"w")
        #txt.write(head)
        #for row in lst:
            #for obj in row:
                #txt.write(obj)
            #txt.write("/n")
            #txt.close
        for i in range(len(lst)):
            for j in range(len(lst[0])):
                line[i][j] = lst[i][j]