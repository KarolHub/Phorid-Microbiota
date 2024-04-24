add_library('pdf')

#======================================================================================
# This is a script for producing population piecharts and heatmaps for the SPH article
#======================================================================================



#_____________________What you need to include in the input file______________________
#======================================================================================
#The input file should be a table in a .txt format with tabulation as separators
#The script assumes the data format:
#first row - species names
#first column - names of trap/habitat
#second and further columns - host species numbers
#======================================================================================



#___________________________________Table importing___________________________________
#======================================================================================
#Please input the path to your data file and its name below (it should be in .txt format):
input_path = "C:\OneDrive\OneDrive - Uniwersytet Jagielloński\Thaumiel\Processing\Article_SPH_Piechart_Host_Distribution"
file_name = "Piechart_data.txt"
#======================================================================================



#___________________________________Saving the PDF____________________________________
#======================================================================================
#Please input the output path for your PDF; Add "#" at the beginning to disable saving:
#beginRecord(PDF,"C:/Users/Walka/Downloads/Pie_poster.pdf")
#======================================================================================


#_____________________________________Settings________________________________________
#======================================================================================
#Change pie diameter:
diam=250
gap=10
#======================================================================================
#Change the size of the background and its colour; background(255) for white:
size(1900,950)
background(255)
#======================================================================================
#Change offset:
x=250
y=150

wrap=1600
hole=120
hole_color = (255)
text_color = 0



sqr_size = 9
sqr_border = 1
#====================================================================================
#Change border colour and width or delete "#" in the last line to erase borders:
#stroke(0) #border colour - 0 for black, 
#strokeWeight(0) #border size

#How many species colors in the legend?
spec_color = 35

#Border size
border = 1.5

#Internal borders
internal_border = 0

#======================================================================================
#Change font size:
textSize(10)
#Change label size:
labelSize = 16
#======================================================================================
#Colour pallete for the host species:


palette=["#9A0C12","#E69500","#4A62a9","#277D22","#A3B1D9","#F3D34C","#A3E6CB","#E0C361","#8ACFE1","#41C70B","#C53B41","#6B2CE2","#113295","#9A9900","#800080","#C6A8E2","#D5757E","#E2DF74","#996A07","#4C2900",   "#008080","#52ED52","#22A9D8","#FF69B4","#FF6347",      "#1F1F1F","#B1B1B1","#A9A9A9","#DBDBDB","#5D5D5D","#B5B5B5","#959595","#191919","#DFDFDF","#6D6D6D","#575757","#737373","#555555","#8B8B8B","#939393","#BBBBBB","#878787","#3B3B3B","#212121","#616161","#A3A3A3","#8F8F8F","#C3C3C3","#717171","#3D3D3D","#DDDDDD","#373737","#2D2D2D","#8D8D8D","#353535","#EDEDED","#6F6F6F","#CDCDCD","#434343","#777777","#4B4B4B","#5B5B5B","#ADADAD","#A5A5A5","#474747","#A7A7A7","#7D7D7D","#E9E9E9","#454545","#E3E3E3","#A1A1A1","#D5D5D5","#9B9B9B","#B7B7B7","#B3B3B3","#696969","#919191","#999999","#636363","#ABABAB","#4D4D4D","#757575","#858585","#595959","#E5E5E5","#111111","#F1F1F1","#272727","#4F4F4F","#3F3F3F","#1D1D1D","#D3D3D3","#2F2F2F","#797979","#2B2B2B","#EBEBEB","#1B1B1B","#7B7B7B","#313131","#393939","#818181","#E1E1E1","#676767","#9D9D9D","#C1C1C1","#D9D9D9","#6B6B6B","#171717","#979797","#D7D7D7","#333333","#151515","#B9B9B9","#252525","#7F7F7F","#292929","#BDBDBD","#232323","#656565","#5F5F5F","#898989","#414141","#C7C7C7","#EFEFEF","#838383","#CBCBCB","#BFBFBF","#494949","#515151","#CFCFCF","#9F9F9F","#131313","#535353","#C5C5C5","#D1D1D1","#C9C9C9","#E7E7E7","#AFAFAF","#414141","#C7C7C7","#EFEFEF","#838383","#CBCBCB","#BFBFBF","#494949","#515151","#CFCFCF","#9F9F9F","#131313","#535353","#C5C5C5","#D1D1D1","#C9C9C9","#E7E7E7","#AFAFAF","#414141","#C7C7C7","#EFEFEF","#838383","#CBCBCB","#BFBFBF","#494949","#515151","#CFCFCF","#9F9F9F","#131313","#535353","#C5C5C5","#D1D1D1","#C9C9C9","#E7E7E7","#AFAFAF","#414141","#C7C7C7","#EFEFEF","#838383","#CBCBCB","#BFBFBF","#494949","#515151","#CFCFCF","#9F9F9F","#131313","#535353","#C5C5C5","#D1D1D1","#C9C9C9","#E7E7E7","#AFAFAF","#414141","#C7C7C7","#EFEFEF","#838383","#CBCBCB","#BFBFBF","#494949","#515151","#CFCFCF","#9F9F9F","#131313"]

#prev_palette=["#2A7B12","#14208C","#AC0E13","#ed1c24","#3F50E4","#4CDF20","#F58286","#24CAE0","#B2B9F4","#B8F2A6","#FF9A00","#CFADF3","#FFC773","#FFF673","#FFEF00","#B3A700","#8732E2","#A8EAF3","#B36B00","#592f00",         "#1F1F1F","#B1B1B1","#A9A9A9","#DBDBDB","#5D5D5D","#B5B5B5","#959595","#191919","#DFDFDF","#6D6D6D","#575757","#737373","#555555","#8B8B8B","#939393","#BBBBBB","#878787","#3B3B3B","#212121","#616161","#A3A3A3","#8F8F8F","#C3C3C3","#717171","#3D3D3D","#DDDDDD","#373737","#2D2D2D","#8D8D8D","#353535","#EDEDED","#6F6F6F","#CDCDCD","#434343","#777777","#4B4B4B","#5B5B5B","#ADADAD","#A5A5A5","#474747","#A7A7A7","#7D7D7D","#E9E9E9","#454545","#E3E3E3","#A1A1A1","#D5D5D5","#9B9B9B","#B7B7B7","#B3B3B3","#696969","#919191","#999999","#636363","#ABABAB","#4D4D4D","#757575","#858585","#595959","#E5E5E5","#111111","#F1F1F1","#272727","#4F4F4F","#3F3F3F","#1D1D1D","#D3D3D3","#2F2F2F","#797979","#2B2B2B","#EBEBEB","#1B1B1B","#7B7B7B","#313131","#393939","#818181","#E1E1E1","#676767","#9D9D9D","#C1C1C1","#D9D9D9","#6B6B6B","#171717","#979797","#D7D7D7","#333333","#151515","#B9B9B9","#252525","#7F7F7F","#292929","#BDBDBD","#232323","#656565","#5F5F5F","#898989","#414141","#C7C7C7","#EFEFEF","#838383","#CBCBCB","#BFBFBF","#494949","#515151","#CFCFCF","#9F9F9F","#131313","#535353","#C5C5C5","#D1D1D1","#C9C9C9","#E7E7E7","#AFAFAF","#414141","#C7C7C7","#EFEFEF","#838383","#CBCBCB","#BFBFBF","#494949","#515151","#CFCFCF","#9F9F9F","#131313","#535353","#C5C5C5","#D1D1D1","#C9C9C9","#E7E7E7","#AFAFAF","#414141","#C7C7C7","#EFEFEF","#838383","#CBCBCB","#BFBFBF","#494949","#515151","#CFCFCF","#9F9F9F","#131313","#535353","#C5C5C5","#D1D1D1","#C9C9C9","#E7E7E7","#AFAFAF","#414141","#C7C7C7","#EFEFEF","#838383","#CBCBCB","#BFBFBF","#494949","#515151","#CFCFCF","#9F9F9F","#131313","#535353","#C5C5C5","#D1D1D1","#C9C9C9","#E7E7E7","#AFAFAF","#414141","#C7C7C7","#EFEFEF","#838383","#CBCBCB","#BFBFBF","#494949","#515151","#CFCFCF","#9F9F9F","#131313"]
#alt_palette=["#2A7B12","#4CDF20","#AC0E13","#14208C","#532b00","#3F50E4","#ed1c24","#B36B00","#8732E2","#8B8B8B","#F58286","#24CAE0","#3B3B3B","#6D6D6D","#B2B9F4","#B3A700","#E9E9E9","#A8EAF3","#B7B7B7","#DBDBDB","#FFF673","#B1B1B1","#B8F2A6","#FF9A00","#575757","#FFEF00","#CFADF3","#B5B5B5","#1F1F1F","#212121","#616161","#A9A9A9","#FFC773","#939393","#3D3D3D","#777777","#4B4B4B","#B3B3B3","#EBEBEB","#BBBBBB","#1B1B1B","#737373","#191919","#DDDDDD","#454545","#373737","#2D2D2D","#7B7B7B","#DFDFDF","#5B5B5B","#8D8D8D","#ADADAD","#313131","#696969","#A3A3A3","#878787","#353535","#8F8F8F","#919191","#EDEDED","#6F6F6F","#A5A5A5","#959595","#C3C3C3","#555555","#999999","#E3E3E3","#717171","#636363","#ABABAB","#393939","#4D4D4D","#757575","#818181","#474747","#858585","#E1E1E1","#595959","#E5E5E5","#111111","#676767","#F1F1F1","#9D9D9D","#272727","#C1C1C1","#5D5D5D","#CDCDCD","#D9D9D9","#6B6B6B","#4F4F4F","#3F3F3F","#171717","#979797","#A7A7A7","#D7D7D7","#333333","#1D1D1D","#151515","#A1A1A1","#D3D3D3","#B9B9B9","#252525","#7F7F7F","#292929","#D5D5D5","#2F2F2F","#434343","#BDBDBD","#797979","#2B2B2B","#232323","#656565","#9B9B9B","#5F5F5F","#7D7D7D","#898989","#414141","#C7C7C7","#EFEFEF","#838383","#CBCBCB","#BFBFBF","#494949","#515151","#CFCFCF","#9F9F9F","#131313","#535353","#C5C5C5","#D1D1D1","#C9C9C9","#E7E7E7","#AFAFAF","#7F7F7F","#292929","#D5D5D5","#2F2F2F","#434343","#BDBDBD","#797979","#2B2B2B","#232323","#656565","#9B9B9B","#5F5F5F","#7D7D7D","#898989","#414141","#C7C7C7","#EFEFEF","#838383","#CBCBCB","#BFBFBF","#494949","#515151","#CFCFCF","#9F9F9F","#131313","#535353","#C5C5C5","#D1D1D1","#C9C9C9","#E7E7E7","#AFAFAF","#7F7F7F","#292929","#D5D5D5","#2F2F2F","#434343","#BDBDBD","#797979","#2B2B2B","#232323","#656565","#9B9B9B","#5F5F5F","#7D7D7D","#898989","#414141","#C7C7C7","#EFEFEF","#838383","#CBCBCB","#BFBFBF","#494949","#515151","#CFCFCF","#9F9F9F","#131313","#535353","#C5C5C5","#D1D1D1","#C9C9C9","#E7E7E7","#AFAFAF"]
#======================================================================================


#OK, let's begin!


#The sacred starting ritual which imports and splits the file into rows
import os
os.chdir(input_path)
input = open(file_name,"r")
data = []
for row in input:
    Line=[]
    Line.append(row.strip().split("\t"))
    data += Line
input.close()


#assign color to a species
pal=0
colors_of_species = {}
for species in data[0][1:]:
    #print(species)
    new_dict = {species : palette[pal]}
    colors_of_species.update(new_dict)
    pal+=1



#Main part start
ellipseMode(CENTER)
strokeJoin(BEVEL)
xx=x
yy=y


#doesn't use the first row with species names
for site in data[1:]:
    stroke(0)
    strokeWeight(border)
    noFill()
    circle(xx,yy,diam)
    
    #calculate the number of individuals in a site
    total_site = sum(map(int, site[1:]))
    start=0
    finish=0

    #This part sorts the colors so that each part of the pie chart is smaller than the previous one. Keeps the correct species colours.
    numbers_list = map(int, site[1:])
    species_list = data[0][1:]
    zipped_number_species = zip(numbers_list,species_list)
    sorted_zipped_number_species = sorted(zipped_number_species, reverse=True)
    sorted_numbers, sorted_species = zip(*sorted_zipped_number_species)
    for i in range(len(sorted_numbers)):
        species = int(sorted_numbers[i])
        if species == 0:
            pass
        else:
            finish += species
            spec_col= sorted_species[i]
            fill(colors_of_species[spec_col])
            if internal_border == 0:
                noStroke()
            else:
                strokeWeight(internal_border) 
            arc(xx,yy,diam,diam,float(start)/total_site*2*PI-PI/2,float(finish)/total_site*2*PI-PI/2,3)
            fill(0)    
            start += species                
    
    
    #This is used for making a white circle in the middle
    if hole == 0:
        pass
    else:
        noFill()
        stroke(0)
        strokeWeight(border)
        circle(xx,yy,diam)
        fill(hole_color)
        circle(xx,yy,hole)
        textAlign(CENTER, CENTER)
        fill(text_color)
        text(site[0],xx,yy)
        text(("n= " + str(total_site)),xx,yy+15)
    xx += diam + gap
    if xx > wrap:
        yy += diam + gap
        xx = x
xx=x


"""
#alternative simple legend comment out the heatmap to allow
for i in range(len(data[0][0:spec_color])):
    fill(palette[i])
    square(50,550+(i*11),10)
    fill(0)
    text(data[0][i+1],80,554+(i*11))
"""


#The heatmap at the bottom:
textSize(sqr_size)



pop_shades={0:"#FFFFFF", 1:"#F5F5F5", 2:"#BDBDBD", 3:"#7F7F7F", 4:"#404040", 5:"#000000"}
strokeWeight(sqr_border)


#heatmap squares function:
def legend_sqr():
    square(xx+(i*sqr_size)-(0.5*diam),yy,sqr_size-2)
    

for row in data:
    fill(0)
    textAlign(RIGHT)
    text(row[0],xx-(0.5*diam)-3,yy+7)
    if row == data[0]:
        for i in range(len(row[1:])):
            sample=row[i+1]
            textAlign(LEFT)
            fill(0)
            rotate(3*PI/2)
            text(sample,-yy,xx + (i*sqr_size)-(0.5*diam) + sqr_size-2)
            rotate(-3*PI/2)
            noStroke()
            fill(palette[i])
            square(xx+(i*sqr_size)-(0.5*diam),yy,sqr_size)
        yy+=sqr_size+2
        xx=x
    else:
        for i in range(len(row[1:])):
            sample=int(row[i+1])
            strokeWeight(0.5)
            stroke(0)
            if sample == 0:
                stroke(200)
                fill(pop_shades[0])
                legend_sqr()
            elif sample == 1:
                fill(pop_shades[1])
                legend_sqr()
            elif 2 <= sample <= 4:
                fill(pop_shades[2])
                legend_sqr()
                pass
            elif 5 <= sample <= 9:
                fill(pop_shades[3])
                legend_sqr()
                pass
            elif 10 <= sample <= 19:
                fill(150)
                legend_sqr()
                pass
            elif sample >= 20:
                fill(pop_shades[5])
                legend_sqr()
                pass
        yy+=sqr_size
        xx=x


endRecord()
