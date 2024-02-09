import warnings
import pyttsx3
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from ict_voice import rec_audio, say_hello, say_bye

warnings.filterwarnings("ignore")

engine = pyttsx3.init()
voices = engine.getProperty('voices')  # getting details of current voice
# engine.setProperty('voice', voices[0].id)   #changing index,  changes voices, 0 for male
engine.setProperty('voice', voices[0].id)  # changing index, changes voices, 1 for female

Answer_tag = ["yes", "yep", "yeah"]


def talk(audio):
    engine.say(audio)
    engine.runAndWait()


def pizza():
    driver = webdriver.Chrome(r"C:\Users\Dharshini\Desktop\chromedriver.exe")
    driver.maximize_window()
    talk("Opening Dominos")

    driver.get('https://www.dominos.co.in/')
    sleep(2)

    talk("Getting ready to order")
    driver.get(
        "https://m.dominos.co.in/changeAddress?src=brand&_ga=2.251239366.1331325642.1667537779-602849658.1666749109")
    sleep(2)

    talk("Finding your location")

    talk("Entering your location")
    inp = driver.find_element(by=By.XPATH,
                              value='//*[@id="__next"]/div/div[1]/div[2]/div/div[1]/div/div[2]/div/div[1]/div[2]/div/div[1]/input')
    inp.click()
    inp.send_keys("suthanthira ponvizha")
    sleep(2)

    talk("choosing your location")
    loc = driver.find_element(by=By.CLASS_NAME,
                              value='lst-wrpr')
    loc.click()
    sleep(2)

    talk("getting into the menu page")
    driver.get('https://pizzaonline.dominos.co.in/menu')
    sleep(2)

    talk("Logging in")


    login = driver.find_element(by=By.XPATH,
    value='//*[@id="__next"]/div/div/div[1]/div[1]/div/div[3]/div[3]/div[1]/div[1]')
    login.click()
    sleep(2)
    driver.find_element(by=By.XPATH,
    value='//*[@id="__next"]/div/div/div[1]/div[1]/div/div[3]/div[3]/div[2]/div/div[3]/div/div/div/div[2]/div/form/div[1]/div[2]/input'
    ).send_keys("7904448347")
    sleep(2)

    # #ph_no_submit_BUTTON_XPATH
    driver.find_element(by=By.XPATH,
    value='//*[@id="__next"]/div/div/div[1]/div[1]/div/div[3]/div[3]/div[2]/div/div[3]/div/div/div/div[2]/div/form/div[2]/input'
    ).click()
    sleep(2)

    talk("What is your OTP")
    sleep(3)

    otp_log = rec_audio()
    print("Your OTP is "+otp_log)
    talk(otp_log)
    driver.find_element(by=By.XPATH,
    value='//*[@id="__next"]/div/div/div[1]/div[1]/div/div[3]/div[3]/div[2]/div/div[3]/div/div/div/div[2]/div/div/div/div[1]/input'
    ).send_keys(otp_log)

    sleep(2)

    #otp_submit_BUTTON_XPATH
    driver.find_element(by=By.XPATH,
    value='//*[@id="__next"]/div/div/div[1]/div[1]/div/div[3]/div[3]/div[2]/div/div[3]/div/div/div/div[2]/div/div/div/div[2]/div[2]/button/span'
    ).click()

    sleep(2)

    talk("Do you want me to order from your favourites?")
    query_fav = rec_audio()

    print("Add favourites ?" + query_fav)
    if "yes" in query_fav:
        try:
            # peper barbeque chik

            driver.find_element(by=By.XPATH,
                                value='//*[@id="mn-lft"] / div[2] / div / div[17] / div / div / div[2] / div[3] / div / button / span'

                                ).click()
            sleep(1)
        except:
            talk("The entered OTP is incorrect.")
            exit()

        talk("Adding your favorites to cart")

        talk("Do you want me to add extra cheese to your pizza?")
        ex_cheese = rec_audio()
        if "yes" in ex_cheese:
            talk("Extra cheese added")
            driver.find_element(by=By.XPATH,
                                value='// * [ @ id = "mn-lft"] / div[2] / div / div[1] / div / div / div[2] / div[3] / div[2] / button'

                                ).click()
        elif "no" in ex_cheese:
            driver.find_element(by=By.XPATH,
                                value='// * [ @ id = "mn-lft"] / div[2] / div / div[1] / div / div / div[2] / div[3] / div[1] / button / span'

                                ).click()
            sleep(1)
        else:
            talk("I don’t know that")
            driver.find_element(by=By.XPATH,
                                value='// * [ @ id = "mn-lft"] / div[2] / div / div[1] / div / div / div[2] / div[3] / div[1] / button / span'

                                ).click()

        #pepsi
        driver.find_element(by=By.XPATH,
        value='// * [ @ id = "mn-lft"] / div[12] / div / div[1] / div / div / div[2] / div[2] / div / button'

        ).click()
        sleep(1)

        talk("Would you like to increase the  quantity?")
        qty = rec_audio()
        qty_pizza = 0
        qty_pepsi = 0
        if "yes" in qty:
            talk("Would you like to increase the quantity of pizza?")
            wh_qty = rec_audio()
            sleep(1)
            if "yes" in wh_qty:
                talk("How many more pizzas would you like to add?")
                try:

                    qty_pizza = rec_audio()
                    sleep(1)
                    qty_pizza = int(qty_pizza)
                    if qty_pizza > 0:
                        talk_piz = f"Adding {qty_pizza} more pizzas"
                        talk(talk_piz)
                        for i in range(qty_pizza):
                            driver.find_element(by=By.XPATH,

                                                value='//*[@id="mn-lft"]/div/div/div[1]/div[2]/div[2]//div[2]/div/div/div[1]/div[1]/div'
                                                ).click()
                except:
                    talk("I don’t know that")
            else:
                pass

            talk("Would you like to increase the quantity of pepsi?")

            pep_qty = rec_audio()
            sleep(1)
            if "yes" in pep_qty:
                talk("How many more pepsis would you like to add?")
                try:
                    qty_pepsi = 0
                    qty_pepsi = rec_audio()

                    qty_pepsi = int(qty_pepsi)
                    if qty_pepsi > 0:
                        talk_pep = f"Adding {qty_pepsi} more pepsi"
                        talk(talk_pep)
                        for i in range(qty_pepsi):
                            driver.find_element(by=By.XPATH,

                                                value='//*[@id="mn-lft"]/div/div/div[1]/div[2]/div[2]/div[2]/div[2]/div/div/div[1]/div[2]/div/div/div[2]/div/div/div[2]'
                                                ).click()
                except:
                    talk("I don’t know that")
            else:
                pass
        elif "no" in qty:
            pass
        total_pizza = qty_pizza + 1
        total_pepsi = qty_pepsi + 1
        tell_num = f"This is your list of orders. {total_pizza} Pizzas and {total_pepsi} Pepsis. Do you want to checkout?"
        talk(tell_num)
        check_order = rec_audio()
        sleep(1)

        if "yes" in check_order:

            total = driver.find_element(By.XPATH,

                                        value='//*[@id="__next"]/div/div/div[1]/div[2]/div[2]/div[2]/div[2]/div/div/div[2]/div[1]/span[2]'
                                        ).text
            # total-minicart
            print("Total Price  " + total)
            total_price = f'Total price is {total}'
            talk(total_price)
            sleep(1)

            driver.find_element(by=By.XPATH,
                                value='//*[@id="__next"]/div/div/div[1]/div[2]/div[2]/div[2]/div[2]/div/div/div[2]/div[2]/button'
                                # '//*[]@id="__next"]/div/div/div[1]/div[2]/div[2]/div[2]/div[2]/div/div/div[2]/div[2]/button'
                                ).click()
            sleep(1)

        else:
            exit()

        talk("getting into the cart page")
        driver.get('https://pizzaonline.dominos.co.in/cart')
        sleep(2)

        talk("placing your order")
        driver.find_element(by=By.XPATH,
                            value='//*[ @ id = "__next"]/div/div[1]/div[2]/div[3]/div[2]/div/div[6]/div/div/div[7]/button'
                            # value='//*[@id="__next"]/div/div[1]/div[2]/div[3]/div[2]/div/div[6]/div/div/div[8]/button'
                            ).click()
        sleep(2)

        try:
            talk("Saving your location")
            driver.find_element(by=By.XPATH,
                                value='//*[@id="__next"]/div/div[1]/div[2]/div[3]/div[2]/div/div[3]/div/div[3]/div/div/div[3]/div/div/input'

                                ).click()
            sleep(2)
        except:
            talk("the store is currently offline.")

        talk("Do you want to confirm your order?")
        confirm = rec_audio()
        if "yes" in confirm:
            talk("Thanks for placing your order")
            talk(say_bye(rec_audio))

            driver.find_element(by=By.XPATH,
                                value='//*[@id="__next"]/div/div[1]/div[2]/div[3]/div[2]/div/div[6]/div/div/div[7]/button'

                                ).click()
            sleep(2)
            talk("Your order is placed successfully. Wait for Dominos to deliver your order. Enjoy your day with dominos")
            exit()
        else:
            talk(say_bye("no"))
            exit()
    else:
        talk(say_bye("no"))
        exit()


tocontinue = True
while tocontinue:
    action_end = ["thank you", "bai", "bi", "bye", "no thanks", "sorry not now"]

    talk("Hi Welcome")
    text = rec_audio()

    hello_reply = say_hello(text)

    text = rec_audio()
    if "yeah" in text or "yes" in text or "yep" in text:
        talk("I  can  order  your  favourites  from  Dominos. Enjoy  your  day  with  dominos")
        pizza()
        tocontinue = False

    elif "no" in text or "quit" in text or "exit" in text:
        talk(say_bye(text))
        exit()
    else:
        talk('Sorry, I dont know that')

#