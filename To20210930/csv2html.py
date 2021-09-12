import csv
def getIdLink(text):
    if text == "":
        return "<p></><p></><p></>動画がありません<p></><p></><p></>"
    r = text.split('open?id=')
    return '<iframe src="https://drive.google.com/file/d/' + r[1] +  '/preview" width="320" height="240" allow="autoplay"></iframe>'

fname = "women_fx" 
csv_file = open("./" + fname + ".csv", "r",  errors="", newline="" )
f_in = csv.reader(csv_file, delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)
header = next(f_in)
print(header)
out = "./" + fname + ".html"
with open(out, mode='w') as f:
    f.write(''''
    <div style="overflow-y:scroll;border: 1px solid #000;">''')
    for row in f_in:
        print(row)
        
        link = getIdLink(row[3])

        s = '''
        <div style="margin:0px;padding:0px;" align="center"> 
            {0}位
            <table width="98%" style="border-collapse: collapse;border:1px solid #000000;background-color:#FFFFFF;color:#000000;text-align:left;"><tbody>
            <tr> 
            <td style="border:1px solid #000000;text-align:center;">{1}&nbsp;</td>
            <td style="border:1px solid #000000;text-align:center;">{2}&nbsp;</td>
            <td style="border:1px solid #000000;text-align:center;">{3}&nbsp;</td>
            </tr>
            </tbody></table></div>

            {4}
            
            <div style="margin:0px;padding:0px;" align="center">
            <table width="98%" style="border-collapse: collapse;border:1px solid #000000;background-color:#FFFFFF;color:#000000;text-align:left;"><tbody>
            <tr>
            <td style="border:1px solid #000000;text-align:center;">{5}&nbsp;</td>
            <td style="border:1px solid #000000;text-align:center;">{6}&nbsp;</td>
            <td style="border:1px solid #000000;text-align:center;">{7}&nbsp;</td>
            <td style="border:1px solid #000000;text-align:center;">{8}&nbsp;</td>
            </tr>
            </tbody></table>
        </div>
        <p></>
        <hr>
        <p></>
        '''.format(row[8], row[0], row[1], row[2], link, row[5], row[6], row[7], row[4])
        f.write(s)
    f.write(''''
    </div>''')

