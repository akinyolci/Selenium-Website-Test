# import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.safari.options import Options

options = Options()
options.page_load_strategy = 'eager'
driver = webdriver.Safari()
driver.implicitly_wait(0.1)
try:
    driver.get("http://techcrunch.com")
    print(len(driver.find_element(By.TAG_NAME, 'html').get_attribute('innerHTML'))*8/1024/1024)
    print(driver.title)
    articles = driver.find_elements(By.TAG_NAME, 'article')
    print("Number of articles:", len(articles))
    posts = driver.find_elements(By.CLASS_NAME, 'post-block')
    print("Number of post-block:", len(posts))
    authors = [i.find_elements(By.CLASS_NAME, 'river-byline__authors') for i in posts]
    print("Number of river-byline__authors:", len(authors))
    for i in authors:
        for j in i:
            print(j.find_element(By.TAG_NAME, 'a').text)
    pictures = [i.find_elements(By.TAG_NAME, 'img') for i in posts]
    print("Number of pictures:", len(pictures))
    linksInPosts = {}
    for article in posts:
        authorLen = len(article.find_elements(By.CLASS_NAME, 'river-byline__authors'))
        pictureLen = len(article.find_elements(By.TAG_NAME, 'img'))
        if authorLen != 1:
            print("Problem with article author: ", article)
            print(authorLen)
            print(article.get_attribute('innerHTML'))

        if pictureLen != 1:
            print("Problem with article picture: ", article)
            print(pictureLen)

        linksInPosts[article] = {post.get_attribute('href'):0 for post in article.find_elements(By.TAG_NAME, 'a')}
    print(len(linksInPosts))
    for links in linksInPosts:
        print(linksInPosts[links])
        for link in linksInPosts[links]:
            print(link)
            driver.get(link)
            linksInPosts[links][link] = len(driver.find_element(By.TAG_NAME, 'html').get_attribute('innerHTML'))*8/1024/1024
            print(linksInPosts[links][link])
            print(len(driver.page_source)*8/1024/1024)



except Exception as e:
    raise e
finally:
    driver.quit()
