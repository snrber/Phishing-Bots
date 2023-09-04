
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait

#Create driver instance "browser"
browser = webdriver.Firefox()
browser.implicitly_wait(5)
browser.get("https://www.twitter.com/login")

#Set wait time
wait = WebDriverWait(browser, 10)

#Tweet to be printed
tweet = "For opportunities email me: mildbagels5@gmail.com"
    
#Login 
username_input = browser.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input")
username_input.send_keys("BagelsMild")

next_signin_button = browser.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div")
next_signin_button.click()

password_input = browser.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input")
password_input.send_keys("UB~p`3K}`e2X")

login_button = browser.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div/div/div")
login_button.click()

#Select explore option on homepage
hashtag_explore_button = browser.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/header/div/div/div/div[1]/div[2]/nav/a[2]/div/div[2]/span")
hashtag_explore_button.click()

#Select trending tab
trending_button = browser.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[1]/div[1]/div[2]/nav/div/div[2]/div/div[2]/a/div/div/span")
trending_button.click()

#Refuse non-essential cookies
refuse_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.r-1sw30gj:nth-child(2)")))
browser.execute_script("arguments[0].click();", refuse_button)

#Select trending topics
#trending_1 = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/section/div/div/div[3]")))
#trending_1.click()

trending_topics = browser.find_elements(By.XPATH, "//div[@data-testid='trend']")
browser.execute_script("arguments[0].click();", trending_topics[0])

#Create iterator for top 50 current posts
"""
for i in range(0, 49):
    
    #Create initial list of posts
    while i == 0:
        posts = browser.find_elements(By.XPATH, "//div[@data-testid='tweetText']")
        break 
        
    browser.execute_script("arguments[0].click();", posts[i])

    #Type and send tweet
    wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@data-testid='tweetTextarea_0']"))).send_keys(tweet)
    reply_button = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@data-testid='tweetButtonInline']")))
    browser.execute_script("arguments[0].click();", reply_button)
    print("Post", i, ":", posts[i]) #Print reply count

    #Go back to trending page and update posts
    browser.execute_script("window.history.go(-1)") #When you go back, DOM goes stale aka posts list needs to be updated, hence next line
    browser.execute_script("window.scrollBy(0, 500)")
    sleep(2)


    #Scroll to next tweet
    posts = browser.find_elements(By.XPATH, "//div[@data-testid='tweetText']")
"""

posts = browser.find_elements(By.XPATH, "//div[@data-testid='tweetText']")

for i in range(0, 49):
    posts = browser.find_elements(By.XPATH, "//div[@data-testid='tweetText']")

    #When next post is within range, execute script
    if (i+1) <= len(posts):
        browser.execute_script("arguments[0].click();", posts[i])

        #Type and send tweet
        wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@data-testid='tweetTextarea_0']"))).send_keys(tweet)
        reply_button = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@data-testid='tweetButtonInline']")))
        browser.execute_script("arguments[0].click();", reply_button)
        print("Post", i, ":", posts[i]) #Print reply count

        #Go back to trending page and update posts
        browser.execute_script("window.history.go(-1)") #When you go back, DOM goes stale aka posts list needs to be updated, hence next line
        browser.execute_script("window.scrollBy(0, 500)")
        sleep(2)

        #Update DOM
        posts = browser.find_elements(By.XPATH, "//div[@data-testid='tweetText']")

    #Go back to trending tab to get to next trending topic once next post is out of range
    elif (i+1) > len(posts):
        back_to_trending = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@data-testid='app-bar-back']")))
        browser.execute_script("arguments[0].click();", back_to_trending)
        #Update trending_topics list
        trending_topics = browser.find_elements(By.XPATH, "//div[@data-testid='trend']")
        browser.execute_script("arguments[0].click();", trending_topics[1])
        i = len(posts)

        

