from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from time import sleep

def main():
    # Set up Facebook login account name and password
    account = "sample@gmail.com"
    password = "sample_pwd"
	
    # Set up Facebook groups to post, you must be a member of the group
    public_groups_links_list = [
		"https://www.facebook.com/groups/1906968099623546/?ref=timeline",
		"https://www.facebook.com/groups/theyogaofsinususoidalresonance/?ref=timeline",
		"https://www.facebook.com/groups/1336081099910053/?ref=timeline",
		"https://www.facebook.com/groups/meditator/?ref=timeline",
		"https://www.facebook.com/groups/HealthAfterForty/?ref=timeline",
		"https://www.facebook.com/groups/629555443733186/?ref=timeline",
		"https://www.facebook.com/groups/712499075531553/?ref=timeline",
		"https://www.facebook.com/groups/2485699931753569/?ref=timeline",
		"https://www.facebook.com/groups/yogacommunitytoronto/?ref=timeline",
		"https://www.facebook.com/groups/praana/?ref=timeline",
		"https://www.facebook.com/groups/157497455091936/?ref=timeline",
		"https://www.facebook.com/groups/842141209593972/?ref=timeline",
		"https://www.facebook.com/groups/DMVNepaliGroup/?ref=timeline",
		"https://www.facebook.com/groups/indiansinvirginia/?ref=timeline",
		"https://www.facebook.com/groups/85588244403/?ref=timeline",
		"https://www.facebook.com/groups/239260300149139/?ref=timeline",
		"https://www.facebook.com/groups/270020646495756/?ref=timeline",
		"https://www.facebook.com/groups/567836446732595/?ref=timeline",
		"https://www.facebook.com/groups/indiansinvienna/?ref=timeline",
		"https://www.facebook.com/groups/127745834506809/?ref=timeline",
		"https://www.facebook.com/groups/131169024015971/?ref=timeline",
		"https://www.facebook.com/groups/366512203537001/?ref=timeline",
		"https://www.facebook.com/groups/1449041095366558/?ref=timeline",
		"https://www.facebook.com/groups/eventsindmv/?ref=timeline",
		"https://www.facebook.com/groups/204564680056821/?ref=timeline",
		"https://www.facebook.com/groups/1690791227662150/?ref=timeline",
		"https://www.facebook.com/groups/121565584706931/?ref=timeline",
		"https://www.facebook.com/groups/TTDBethesda/?ref=timeline",
		"https://www.facebook.com/groups/550763698288195/?ref=timeline",
		"https://www.facebook.com/groups/39293146066/?ref=timeline",
		"https://www.facebook.com/groups/jhuigsa/?ref=timeline",
		"https://www.facebook.com/groups/gmuisa/?ref=timeline",
		"https://www.facebook.com/groups/2200235840/?ref=timeline",
		"https://www.facebook.com/groups/iac.md/?ref=timeline",
		"https://www.facebook.com/groups/197746146903684/?ref=timeline"
    ]
	
    private_groups_links_list = [
		"https://www.facebook.com/groups/199599183883851/",
		"https://www.facebook.com/groups/787804624600044/",
		"https://www.facebook.com/groups/metrowestva/",
		"https://www.facebook.com/groups/viennaic/",
		"https://www.facebook.com/groups/407837970028823/",
		"https://www.facebook.com/groups/tirangavcu/",
		"https://www.facebook.com/groups/IndianGrads/",
		"https://www.facebook.com/groups/185486058172353/",
		"https://www.facebook.com/groups/RestonCommunityGroup/",
		"https://www.facebook.com/groups/churchinbethesda/",
		"https://www.facebook.com/groups/Indians.DCMetro/",
		"https://www.facebook.com/groups/circletowersstudentsforum/",
		"https://www.facebook.com/groups/268731623280985/",
		"https://www.facebook.com/groups/433598450010836/",
		"https://www.facebook.com/groups/foreign.in.vienna2/",
		"https://www.facebook.com/groups/FrontRoyalHomeschooling/",
		"https://www.facebook.com/groups/1578722052447576/",
		"https://www.facebook.com/groups/305237466169342/",
		"https://www.facebook.com/groups/400665160400083/",
		"https://www.facebook.com/groups/122710658251699/",
		"https://www.facebook.com/groups/912214545572277/",
		"https://www.facebook.com/groups/228921327592454/",
		"https://www.facebook.com/groups/MeditationGroup/"
	]
	
    new_groups_link_list = [
    	"https://www.facebook.com/groups/109848329099374/",
		"https://www.facebook.com/groups/1256095427763119/",
		"https://www.facebook.com/groups/2624368754464697/",
		"https://www.facebook.com/groups/nagendraprabu/",
		"https://www.facebook.com/groups/399158900422380/",
		"https://www.facebook.com/groups/1660700764179553/",
		"https://www.facebook.com/groups/1989335744470765/",
		"https://www.facebook.com/groups/462161250482341/",
		"https://www.facebook.com/groups/273110826860297/",
		"https://www.facebook.com/groups/399207704104588/",
		"https://www.facebook.com/groups/advancedteachings/",
		"https://www.facebook.com/groups/275219976362306/",
		"https://www.facebook.com/groups/1209341489177314/",
		"https://www.facebook.com/groups/222009931151122/",
		"https://www.facebook.com/groups/1849790778598032/",
		"https://www.facebook.com/groups/NJNYIndians/",
		"https://www.facebook.com/groups/NJNYIndians/",
		"https://www.facebook.com/groups/2044075505814411/",
		"https://www.facebook.com/groups/512762412965068/",
		"https://www.facebook.com/groups/627563244268478/",
		"https://www.facebook.com/groups/223929157772825/",
		"https://www.facebook.com/groups/627563244268478/",
		"https://www.facebook.com/groups/meditationtechniquesforbeginners/",
		"https://www.facebook.com/groups/535924603584727/",
		"https://www.facebook.com/groups/desicollection/",
		"https://www.facebook.com/groups/1054695267885725/",
		"https://www.facebook.com/groups/IndiansinTexas/",
		"https://www.facebook.com/groups/352772894857422/",
		"https://www.facebook.com/groups/194530433941877/",
		"https://www.facebook.com/groups/energyandemotion/",
		"https://www.facebook.com/groups/1229821433717970/",
		"https://www.facebook.com/groups/478403522812003/",
		"https://www.facebook.com/groups/752492878172960/",
		"https://www.facebook.com/groups/556900785175306/",
		"https://www.facebook.com/groups/1154570404923398/",
		"https://www.facebook.com/groups/110389522305985/",
		"https://www.facebook.com/groups/233092010039560/",
		"https://www.facebook.com/groups/898990246877219/"	
    ]	
    groups_links_list = public_groups_links_list
    groups_links_list.extend(private_groups_links_list)
	groups_links_list.extend(new_groups_link_list)
    # Set up text content to post
    message = "Your Welcome :) \nCome, learn happiness from the best! \nJohn Osborne has been teaching mind/body & stress management techniques since 1975. \nHe serves as the national director of Project Welcome Home Troops, which is dedicated at serving veterans & their families through mind/body practices.\nhttp://tiny.cc/happydmv"
	# Set up paths of images to post
    images_list = ['/Users/harshagarwal/Downloads/JohnCourse.jpeg']

    # Login Facebook
    chrome_options = webdriver.ChromeOptions()
    prefs = {"profile.default_content_setting_values.notifications" : 2}
    chrome_options.add_experimental_option("prefs",prefs)
    chrome_options.add_experimental_option("excludeSwitches", ['enable-automation']);
    chrome_options.add_argument('--ignore-ssl-errors=yes')
    chrome_options.add_argument('--ignore-certificate-errors')
	
    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.get('https://www.facebook.com')
    emailelement = driver.find_element(By.XPATH,'//*[@id="email"]')
    emailelement.send_keys(account)
    passelement = driver.find_element(By.XPATH,'//*[@id="pass"]')
    passelement.send_keys(password)
    loginelement = driver.find_element(By.XPATH,'//*[@id="loginbutton"]')
    loginelement.click()

    # Post on each group
    for group in groups_links_list:
        driver.get(group)
        time.sleep(2)
        try:
            driver.find_element(By.XPATH,'//*[@label="Start Discussion"]').click()
            post_box=driver.find_element_by_css_selector("[name='xhpc_message_text']")
        except:
            post_box=driver.find_element_by_css_selector("[name='xhpc_message_text']")
        post_box.send_keys(message)
        time.sleep(1)
        for photo in images_list:
            photo_element = driver.find_element_by_xpath("//input[@type='file'][@aria-label='Add Photo or Video']")
            #photo_element.click()
            photo_element.send_keys(photo)
            time.sleep(1)
        time.sleep(6)
        post_button = driver.find_element_by_xpath("//*[@class='fbReactComposerAttachmentSelector_MEDIA pas _1fng _51m-']")
        post_button = driver.find_element_by_xpath("//*[contains(text(), 'Post')]")
        post_button = driver.find_element_by_xpath("//*[@class='_1mf7 _4jy0 _4jy3 _4jy1 _51sy selected _42ft']")
        clickable = False
        while not clickable:
            cursor = post_button.find_element_by_tag_name('span').value_of_css_property("cursor")
            if cursor == "pointer":
                clickable = True
            break
        post_button.click()
        time.sleep(10)
    # Close driver
    driver.close()

if __name__ == '__main__':
  main()
