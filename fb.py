from selenium import webdriver

from selenium.webdriver.common.keys import Keys

from itertools import permutations

import time

import sys



driver = webdriver.Firefox()

facebook_username="0942878977"
facebook_password="sao101thang"

print "BBBBBBBBB"
print "BBBBBBBBBBB"
print "BBB      BBB"
print "BBB       BBB"
print "BBB      BBB"
print "BBBBBBBBBBB"
print "BBBBBBBBBBBB"
print "BBB       BBBB"
print "BBB        BBBB"
print "BBB        BBBB"
print "BBB       BBBBB"
print "BBBBBBBBBBBBBB"
print "BBBBBBBBBBBBB\n\n"


global userid
print "Dang tien hanh dang nhap\n"

global userid
def dangNhapFacebook(driver): #truy cap facebook
    driver.get("https://www.facebook.com/")
    time.sleep(3)
    driver.find_element_by_id('email').send_keys(facebook_username) #nhap user
    driver.find_element_by_id('pass').send_keys(facebook_password) #nhap pass
    driver.find_element_by_id("loginbutton").click() #an nut dang nhap
    global all_cookies
    all_cookies = driver.get_cookies()
    html = driver.page_source

#=================================================================================

def thuThapThongTinCaNhan(driver,userid):
	driver.get('https://www.facebook.com/'+str(userid)+'/info')	
	if "We couldn't find anything" in driver.page_source:
		print "[!] Nguoi dung khong cong khai thong tin ca nhan "+url
		return ""
        lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;") #script cuon trang
        match=False
        while(match==False):
                time.sleep(3)
                lastCount = lenOfPage
                lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
                if lastCount==lenOfPage:
                        match=True
	return driver.page_source

#=================================================================================

def thuThapApps(driver,userid):
    driver.get('https://www.facebook.com/search/'+str(userid)+'/apps-used')
    if "We couldn't find anything" in driver.page_source:
        print "[!] Nguoi dung khong cong khai app"
        return ""
    else:
            lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;") #script cuon trang
            match=False
            while(match==False):
                    time.sleep(3)
                    lastCount = lenOfPage
                    lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
                    if lastCount==lenOfPage:
                            match=True
            return driver.page_source

#=================================================================================

def thuThapBan(driver,userid):
	driver.get('https://www.facebook.com/search/'+str(userid)+'/friends')
	if "We couldn't find anything" in driver.page_source:
		print "[!] Nguoi dung khong cong khai danh sach ban be"
		return ""
	else:
	        lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;") #script cuon trang
       		match=False
        	while(match==False):
        	        time.sleep(3)
               		lastCount = lenOfPage
                	lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
                	if lastCount==lenOfPage:
                	        match=True
		return driver.page_source

#=================================================================================

def thuThapVideos(driver,userid):
	url = 'https://www.facebook.com/search/'+str(userid).strip()+'/videos-by'
	driver.get(url)	
	if "We couldn't find anything" in driver.page_source:
		print "[!] Nguoi dung khong cong khai danh sach video"+url
		return ""
        lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;") 
        match=False
        while(match==False):
                time.sleep(3)
                lastCount = lenOfPage
                lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;") #script cuon trang
                if lastCount==lenOfPage:
                        match=True
	return driver.page_source


#=================================================================================

def thuThapTrangDaLike(driver,userid):
	url = 'https://www.facebook.com/search/'+str(userid)+'/pages-liked'
	driver.get(url)	
	if "We couldn't find anything" in driver.page_source:
		print "[!] Nguoi dung khong cong khai danh sach cac trang da like"+url
		return ""
        lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;") 
        match=False
        while(match==False):
                time.sleep(3)
                lastCount = lenOfPage
                lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;") #script cuon trang
                if lastCount==lenOfPage:
                        match=True
	return driver.page_source

#================================================================================

def thuThapAnhBoiNgDung(driver,userid):
	driver.get('https://www.facebook.com/search/'+str(userid)+'/photos-by')
	if "Sorry, we couldn't find any results for this search." in driver.page_source:
		print "[!] Nguoi dung khong cong khai anh boi nguoi dung"
        lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
        match=False
        while(match==False):
                time.sleep(3)
                lastCount = lenOfPage
                lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
                if lastCount==lenOfPage:
                        match=True
	return driver.page_source

#================================================================================

def thuThapAnhCuaNgDung(driver,userid):
	driver.get('https://www.facebook.com/search/'+str(userid)+'/photos-of')
	if "Sorry, we couldn't find any results for this search." in driver.page_source:
		print "[!] Nguoi dung khong cong khai anh cua nguoi dung"
        lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
        match=False
        while(match==False):
                time.sleep(3)
                lastCount = lenOfPage
                lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
                if lastCount==lenOfPage:
                        match=True
	return driver.page_source

#================================================================================

def thuThapAnhDaLike(driver,userid):
	driver.get('https://www.facebook.com/search/'+str(userid)+'/photos-liked/intersect')
	if "We couldn't find anything" in driver.page_source:
		print "[!] Nguoi dung khong cong khai danh sach cac anh da like"
        lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
        match=False
        while(match==False):
                time.sleep(3)
                lastCount = lenOfPage
                lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
                if lastCount==lenOfPage:
                        match=True
	return driver.page_source

#=================================================================================

def thuThapAnhDaBinhLuan(driver,userid):
	driver.get('https://www.facebook.com/search/'+str(userid)+'/photos-commented/intersect')
	if "Sorry, we couldn't find any results for this search." in driver.page_source:
		print "[!] Nguoi dung khong cong khai danh sach cac anh da binh luan"
        lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
        match=False
        while(match==False):
                time.sleep(3)
                lastCount = lenOfPage
                lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
                if lastCount==lenOfPage:
                        match=True
	return driver.page_source

#==================================================================================

def thuThapNhungNoiDaDen(driver,userid):
	url = 'https://www.facebook.com/search/'+str(userid)+'/places-visited'
	driver.get(url)	
	if "We couldn't find anything" in driver.page_source:
		print "[!] Nguoi dung khong cong khai danh sach cac noi da den"
		return ""
        lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
        match=False
        while(match==False):
                time.sleep(3)
                lastCount = lenOfPage
                lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
                if lastCount==lenOfPage:
                        match=True
	return driver.page_source

#=================================================================================

def thuThapBaiDaDang(driver,userid):
	url = 'https://www.facebook.com/search/'+str(userid)+'/stories-by'
	driver.get(url)	
	if "We couldn't find anything" in driver.page_source:
		print "[!] Nguoi dung khong cong khai danh cac bai da dang"
		return ""
        lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
        match=False
        while(match==False):
                time.sleep(3)
                lastCount = lenOfPage
                lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
                if lastCount==lenOfPage:
                        match=True
	return driver.page_source

#=================================================================================

def main():
   
    dangNhapFacebook(driver)
    while 1:
        print("1. Thu thap nhieu nguoi")
        print("2. Thu thap mot nguoi")
        chon = input("Hay chon mot so tu 1-2 ")
        if chon < 1 or chon > 2:
            print("Hay hoc chu truoc khi hoc tin :)")
        elif chon == 1:
            tenfile=raw_input("Nhap ten file: ")
            f = open(tenfile, "r")
            username=""
            for i in f:
                uid = i
                username = uid
                print("\nTuy chon:")
                print("1. Thu thap thong tin ca nhan cua nguoi dung")
                print("2. Thu thap ung dung cua  cua nguoi dung")
                print("3. Thu thap thong tin danh sach ban be cua nguoi dung")
                print("4. Thu thap thong tin video cua nguoi dung")
                print("5. Thu thap thong tin cac trang nguoi dung da like")
                print("6. Thu thap thong tin cac anh boi nguoi dung")
                print("7. Thu thap thong tin cac anh cua nguoi dung")
                print("8. Thu thap cac anh nguoi dung da like")
                print("9. Thu thap cac anh nguoi dung da binh luan")
                print("10. Thu thap nhung noi da den cua nguoi dung")
                print("11. Thu thap nhung bai da dang cua nguoi dung")
                print("12. Thu thap nguoi tiep theo")

                chon = input("Hay chon mot so tu 1-12 ")

                if chon < 1 or chon > 12:
                    print("Hay hoc chu truoc khi hoc tin :)")
                elif chon == 1:
                    filename = username+'_thongtincanhan.html'
                    print "[*] Dang thu thap thong tin ca nhan cua nguoi dung: "+username
                    html = thuThapThongTinCaNhan(driver,uid)
                    text_file = open(filename, "w")
                    text_file.write(html.encode('utf8'))
                    text_file.close()
                elif chon == 2:
                    filename = username+'_apps.html'
                    print "[*] Dang thu thap ung dung cua nguoi dung: "+username
                    html = thuThapApps(driver,uid)
                    text_file = open(filename, "w")
                    text_file.write(html.encode('utf8'))
                    text_file.close()
                elif chon == 3:
                    filename = username+'_ban.html'
                    print "[*] Dang thu thap thong tin ban cua nguoi dung: "+username
                    html = thuThapBan(driver,uid)
                    text_file = open(filename, "w")
                    text_file.write(html.encode('utf8'))
                    text_file.close()
                elif chon == 4:
                    filename = username+'_video.html'
                    print "[*] Dang thu thap thong tin video cua nguoi dung: "+username
                    html = thuThapVideos(driver,uid)
                    text_file = open(filename, "w")
                    text_file.write(html.encode('utf8'))
                    text_file.close()
                elif chon == 5:
                    filename = username+'_cactrangdalike.html'
                    print "[*] Dang thu thap cac trang nguoi dung: "+username+" da like "
                    html = thuThapTrangDaLike(driver,uid)
                    text_file = open(filename, "w")
                    text_file.write(html.encode('utf8'))
                    text_file.close()
                elif chon == 6:
                    filename = username+'_cacanhboinguoidung.html'
                    print "[*] Dang thu thap cac anh boi nguoi dung: "+username
                    html = thuThapAnhBoiNgDung(driver,uid) 
                    text_file = open(filename, "w")
                    text_file.write(html.encode('utf8'))
                    text_file.close()
                elif chon == 7:
                    filename = username+'_cacanhcuanguoidung.html'
                    print "[*] Dang thu thap cac anh cua nguoi dung: "+username
                    html = thuThapAnhCuaNgDung(driver,uid)
                    text_file = open(filename, "w")
                    text_file.write(html.encode('utf8'))
                    text_file.close()
                elif chon == 8:
                    filename = username+'_cacanhdalike.html'
                    print "[*] Dang thu thap cac anh nguoi dung "+username+" da like"
                    html = thuThapAnhDaLike(driver,uid) 
                    text_file = open(filename, "w")
                    text_file.write(html.encode('utf8'))
                    text_file.close()
                elif chon == 9:
                    filename = username+'_cacanhdabinhluan.html'
                    print "[*] Dang thu thap cac anh nguoi dung da "+username+" binh luan"
                    html = thuThapAnhDaBinhLuan(driver,uid)
                    text_file = open(filename, "w")
                    text_file.write(html.encode('utf8'))
                    text_file.close()
                elif chon == 10:
                    filename = username+'_nhungnoidaden.html'
                    print "[*] Dang thu thap nhung noi da den cua nguoi dung: "+username
                    html = thuThapNhungNoiDaDen(driver,uid)
                    text_file = open(filename, "w")
                    text_file.write(html.encode('utf8'))
                    text_file.close()
                elif chon == 11:
                    filename = username+'_nhungbaidadang.html'
                    print "[*] Dang thu thap nhung bai da dang cua nguoi dung: "+username
                    html = thuThapBaiDaDang(driver,uid)
                    text_file = open(filename, "w")
                    text_file.write(html.encode('utf8'))
                    text_file.close()

                elif chon == 12:
                    continue


        elif chon == 2:
            uid = raw_input("User ID: ")
            username = raw_input("User name: ")
            username = username.strip()
            print "[*] Username:\t"+str(username)
            while 1:
                print("\nTuy chon:")
                print("1. Thu thap thong tin ca nhan cua nguoi dung")
                print("2. Thu thap ung dung cua  cua nguoi dung")
                print("3. Thu thap thong tin danh sach ban be cua nguoi dung")
                print("4. Thu thap thong tin video cua nguoi dung")
                print("5. Thu thap thong tin cac trang nguoi dung da like")
                print("6. Thu thap thong tin cac anh boi nguoi dung")
                print("7. Thu thap thong tin cac anh cua nguoi dung")
                print("8. Thu thap cac anh nguoi dung da like")
                print("9. Thu thap cac anh nguoi dung da binh luan")
                print("10. Thu thap nhung noi da den cua nguoi dung")
                print("11. Thu thap nhung bai da dang cua nguoi dung")
                print("12. Thoat chuong trinh")

                chon = input("Hay chon mot so tu 1-12 ")

                if chon < 1 or chon > 12:
                    print("Hay hoc chu truoc khi hoc tin :)")
                elif chon == 1:
                    filename = username+'_thongtincanhan.html'
                    print "[*] Dang thu thap thong tin ca nhan cua nguoi dung: "+username
                    html = thuThapThongTinCaNhan(driver,uid)
                    text_file = open(filename, "w")
                    text_file.write(html.encode('utf8'))
                    text_file.close()
                elif chon == 2:
                    filename = username+'_apps.html'
                    print "[*] Dang thu thap ung dung cua nguoi dung: "+username
                    html = thuThapApps(driver,uid)
                    text_file = open(filename, "w")
                    text_file.write(html.encode('utf8'))
                    text_file.close()
                elif chon == 3:
                    filename = username+'_ban.html'
                    print "[*] Dang thu thap thong tin ban cua nguoi dung: "+username
                    html = thuThapBan(driver,uid)
                    text_file = open(filename, "w")
                    text_file.write(html.encode('utf8'))
                    text_file.close()
                elif chon == 4:
                    filename = username+'_video.html'
                    print "[*] Dang thu thap thong tin video cua nguoi dung: "+username
                    html = thuThapVideos(driver,uid)
                    text_file = open(filename, "w")
                    text_file.write(html.encode('utf8'))
                    text_file.close()
                elif chon == 5:
                    filename = username+'_cactrangdalike.html'
                    print "[*] Dang thu thap cac trang nguoi dung: "+username+" da like "
                    html = thuThapTrangDaLike(driver,uid)
                    text_file = open(filename, "w")
                    text_file.write(html.encode('utf8'))
                    text_file.close()
                elif chon == 6:
                    filename = username+'_cacanhboinguoidung.html'
                    print "[*] Dang thu thap cac anh boi nguoi dung: "+username
                    html = thuThapAnhBoiNgDung(driver,uid) 
                    text_file = open(filename, "w")
                    text_file.write(html.encode('utf8'))
                    text_file.close()
                elif chon == 7:
                    filename = username+'_cacanhcuanguoidung.html'
                    print "[*] Dang thu thap cac anh cua nguoi dung: "+username
                    html = thuThapAnhCuaNgDung(driver,uid)
                    text_file = open(filename, "w")
                    text_file.write(html.encode('utf8'))
                    text_file.close()
                elif chon == 8:
                    filename = username+'_cacanhdalike.html'
                    print "[*] Dang thu thap cac anh nguoi dung "+username+" da like"
                    html = thuThapAnhDaLike(driver,uid) 
                    text_file = open(filename, "w")
                    text_file.write(html.encode('utf8'))
                    text_file.close()
                elif chon == 9:
                    filename = username+'_cacanhdabinhluan.html'
                    print "[*] Dang thu thap cac anh nguoi dung da "+username+" binh luan"
                    html = thuThapAnhDaBinhLuan(driver,uid)
                    text_file = open(filename, "w")
                    text_file.write(html.encode('utf8'))
                    text_file.close()
                elif chon == 10:
                    filename = username+'_nhungnoidaden.html'
                    print "[*] Dang thu thap nhung noi da den cua nguoi dung: "+username
                    html = thuThapNhungNoiDaDen(driver,uid)
                    text_file = open(filename, "w")
                    text_file.write(html.encode('utf8'))
                    text_file.close()
                elif chon == 11:
                    filename = username+'_nhungbaidadang.html'
                    print "[*] Dang thu thap nhung bai da dang cua nguoi dung: "+username
                    html = thuThapBaiDaDang(driver,uid)
                    text_file = open(filename, "w")
                    text_file.write(html.encode('utf8'))
                    text_file.close()

                elif chon == 12:
                    driver.close()
                    driver.quit
                    sys.exit()
                    return 0

#====================================
    


main()
