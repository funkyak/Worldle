from selenium import webdriver
from  time import sleep
 

class run():
    def __init__(self):

        self.driver = webdriver.Chrome()

    def search(self):   
        
        self.driver.get('https://worldle.teuteuf.fr')
        sleep(2) # sleep to load website

        org = self.driver.find_element_by_xpath('//*[@id="root"]/div[2]/div/div/div[1]/img')
        val = org.get_attribute("src")
        
        next_word = val[val.index(val)+ 44]
        next_word1 = val[val.index(val)+ 45]
        contents = next_word+next_word1
        
        codes = ["ad", "ae", "af", "ag", "ai", "al", "am", "an", "ao", "aq", "ar", "as", "at", "au", "aw", "az", "ba", "bb", "bd", "be", "bf", "bg", "bh", "bi", "bj", "bm", "bn", "bo", "br", "bs", "bt", "bv", "bw", "by", "bz", "ca", "cc", "cd", "cf", "cg", "ch", "ci", "ck", "cl", "cm", "cn", "co", "cr", "cu", "cv", "cx", "cy", "cz", "de", "dj", "dk", "dm", "do", "dz", "ec", "ee", "eg", "eh", "er", "es", "et", "fi", "fj", "fk", "fm", "fo", "fr", "ga", "gb", "gd", "ge", "gf", "gg", "gh", "gi", "gl", "gm", "gn", "gp", "gq", "gr", "gs", "gt", "gu", "gw", "gy", "gz", "hk", "hm", "hn", "hr", "ht", "hu", "id", "ie", "il", "im", "in", "io", "iq", "ir", "is", "it", "je", "jm", "jo", "jp", "ke", "kg", "kh", "ki", "km", "kn", "kp", "kr", "kw", "ky", "kz", "la", "lb", "lc", "li", "lk", "lr", "ls", "lt", "lu", "lv", "ly", "ma", "mc", "md", "me", "mg", "mh", "mk", "ml", "mm", "mn", "mo", "mp", "mq", "mr", "ms", "mt", "mu", "mv", "mw", "mx", "my", "mz", "na", "nc", "ne", "nf", "ng", "ni", "nl", "no", "np", "nr", "nu", "nz", "om", "pa", "pe", "pf", "pg", "ph", "pk", "pl", "pm", "pn", "pr", "ps", "pt", "pw", "py", "qa", "re", "ro", "rs", "ru", "rw", "sa", "sb", "sc", "sd", "se", "sg", "sh", "si", "sj", "sk", "sl", "sm", "sn", "so", "sr", "st", "sv", "sy", "sz", "tc", "td", "tf", "tg", "th", "tj", "tk", "tl", "tm", "tn", "to", "tr", "tt", "tv", "tw", "tz", "ua", "ug", "um", "us", "uy", "uz", "va", "vc", "ve", "vg", "vi", "vn", "vu", "wf", "ws", "xk", "ye", "yt", "za", "zm", "zw"]
        FullName = ["Andorra","United Arab Emirates","Afghanistan","Antigua and Barbuda","Anguilla ","Albania","Armenia","Netherlands Antilles","Angola","Antarctica","Argentina","American Samoa","Austria","Australia","Aruba","Azerbaijan","Bosnia and Herzegovina","Barbados","Bangladesh","Belgium","Burkina Faso","Bulgaria","Bahrain","Burundi","Benin","Bermuda","Brunei","Bolivia","Brazil","Bahamas","Bhutan","Bouvet Island","Botswana","Belarus","Belize","Canada","Cocos [Keeling] Islands","Congo [DRC]","Central African Republic","Congo [Republic]","Switzerland","C??te d'Ivoire","Cook Islands","Chile","Cameroon","China","Colombia","Costa Rica","Cuba","Cape Verde","Christmas Island","Cyprus","Czech Republic","Germany","Djibouti","Denmark","Dominica","Dominican Republic","Algeria","Ecuador","Estonia","Egypt","Western Sahara","Eritrea","Spain","Ethiopia","Finland","Fiji","Falkland Islands [Islas Malvinas]","Micronesia","Faroe Islands","France","Gabon","United Kingdom","Grenada","Georgia","French Guiana","Guernsey","Ghana","Gibraltar","Greenland","Gambia","Guinea","Guadeloupe","Equatorial Guinea","Greece","South Georgia and the South Sandwich Islands","Guatemala","Guam","Guinea-Bissau","Guyana","Gaza Strip","Hong Kong","Heard Island and McDonald Islands","Honduras","Croatia","Haiti","Hungary","Indonesia","Ireland","Israel","Isle of Man","India","British Indian Ocean Territory","Iraq","Iran","Iceland","Italy","Jersey","Jamaica","Jordan","Japan","Kenya","Kyrgyzstan","Cambodia","Kiribati","Comoros","Saint Kitts and Nevis","North Korea","South Korea","Kuwait","Cayman Islands","Kazakhstan","Laos","Lebanon","Saint Lucia","Liechtenstein","Sri Lanka","Liberia","Lesotho","Lithuania","Luxembourg","Latvia","Libya","Morocco","Monaco","Moldova","Montenegro","Madagascar","Marshall Islands","Macedonia [FYROM]","Mali","Myanmar [Burma]","Mongolia","Macau","Northern Mariana Islands","Martinique","Mauritania","Montserrat","Malta","Mauritius","Maldives","Malawi","Mexico","Malaysia","Mozambique","Namibia","New Caledonia","Niger","Norfolk Island","Nigeria","Nicaragua","Netherlands","Norway","Nepal","Nauru","Niue","New Zealand","Oman","Panama","Peru","French Polynesia","Papua New Guinea","Philippines","Pakistan","Poland","Saint Pierre and Miquelon","Pitcairn Islands","Puerto Rico","Palestinian Territories","Portugal","Palau","Paraguay","Qatar","R??union","Romania","Serbia","Russia","Rwanda","Saudi Arabia","Solomon Islands","Seychelles","Sudan","Sweden","Singapore","Saint Helena","Slovenia","Svalbard and Jan Mayen","Slovakia","Sierra Leone","San Marino","Senegal","Somalia","Suriname","S??o Tom?? and Pr??ncipe","El Salvador","Syria","Swaziland","Turks and Caicos Islands","Chad","French Southern Territories","Togo","Thailand","Tajikistan","Tokelau","Timor-Leste","Turkmenistan","Tunisia","Tonga","Turkey","Trinidad and Tobago","Tuvalu","Taiwan","Tanzania","Ukraine","Uganda","U.S. Minor Outlying Islands","United States","Uruguay","Uzbekistan","Vatican City","Saint Vincent and the Grenadines","Venezuela","British Virgin Islands","U.S. Virgin Islands","Vietna","Vanuatu","Wallis and Futuna","Samoa ","Kosovo","Yemen","Mayotte","South Africa","Zambia","Zimbabwe"]
        output = FullName[codes.index(contents)]
        
        input = self.driver.find_element_by_xpath('//*[@id="root"]/div[2]/div/div/div[3]/form/div/div/input')
        input.send_keys(output)

        enter = self.driver.find_element_by_xpath('//*[@id="root"]/div[2]/div/div/div[3]/form/div/button')
        enter.click()

        print(val) # Testing output from the url
        print(contents) #Code output 
        print(output) # Answer that will be inputed onto the website

bot = run()

bot.search()

# Working only using this one file and auto completes and submites. 100% working
