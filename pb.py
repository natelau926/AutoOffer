from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class Posh:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.bot = webdriver.Firefox()

    def login(self):
        bot = self.bot
        bot.get("https://poshmark.com/login")
        time.sleep(2)
        email = bot.find_element_by_name("login_form[username_email]")
        password = bot.find_element_by_name("login_form[password]")
        email.clear()
        password.clear()
        email.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        time.sleep(5)

    def auto_offer(self,link1):
        bot = self.bot
        bot.get(link1)
        try:

            bot.find_element_by_xpath("/html/body/div[1]/main/div[2]/div/div[2]/div[2]/div[4]/div[2]/div/div/button").click()
            time.sleep(1)
            bot.find_element_by_xpath(
                "/html/body/div[1]/main/div[2]/div/div[2]/div[2]/div[4]/div[2]/div/div[2]/div[1]/div[2]/div[2]/div/div[2]/div/button").click()
            time.sleep(1)
            bot.find_element_by_xpath(
                "/html/body/div[1]/main/div[2]/div/div[2]/div[2]/div[4]/div[2]/div/div[2]/div[1]/div[2]/div[2]/form/div[1]/div/i").click()
            time.sleep(1)
            bot.find_element_by_xpath("/html/body/div[1]/main/div[2]/div/div[2]/div[2]/div[4]/div[2]/div/div[2]/div[2]/div[2]/div[2]/div[2]/div/button[1]").click()  # 10%off
            #bot.find_element_by_xpath("/html/body/div[1]/main/div[2]/div/div[2]/div[2]/div[4]/div[2]/div/div[2]/div[2]/div[2]/div[2]/div[2]/div/button[2]").click() #20$off
            #bot.find_element_by_xpath("/html/body/div[1]/main/div[2]/div/div[2]/div[2]/div[4]/div[2]/div/div[2]/div[2]/div[2]/div[2]/div[2]/div/button[3]").click()  # 30$off
            time.sleep(1)
            bot.find_element_by_xpath(
                "/html/body/div[1]/main/div[2]/div/div[2]/div[2]/div[4]/div[2]/div/div[2]/div[2]/div[2]/div[3]/div/button[2]").click()
            time.sleep(1)
            bot.find_element_by_xpath(
                "/html/body/div[1]/main/div[2]/div/div[2]/div[2]/div[4]/div[2]/div/div[2]/div[1]/div[2]/div[2]/form/div[2]/div[1]/div/div[1]").click()
            time.sleep(1)
            bot.find_element_by_xpath(
                "/html/body/div[1]/main/div[2]/div/div[2]/div[2]/div[4]/div[2]/div/div[2]/div[1]/div[2]/div[2]/form/div[2]/div[1]/div/div[2]/ul/li[1]/div").click()
            time.sleep(1)
            bot.find_element_by_xpath(
                "/html/body/div[1]/main/div[2]/div/div[2]/div[2]/div[4]/div[2]/div/div[2]/div[1]/div[2]/div[3]/div/button[2]").click()
            time.sleep(1)

            """
            bot.find_element_by_xpath("/html/body/main/div/div[1]/div[2]/div[3]/form/div[2]/div[1]/div[3]/a").click()
            time.sleep(1)
            bot.find_element_by_xpath("/html/body/main/div/div[5]/div[2]/div/div[2]/a/span").click()
            time.sleep(1)
            bot.find_element_by_id("offer_to_likers_calculator").click()
            time.sleep(1)
            bot.find_element_by_xpath("/html/body/main/div[1]/div[7]/div[2]/div[2]/div[4]").click()  #10%OFF
            time.sleep(1)
            bot.find_element_by_xpath("/html/body/main/div[1]/div[7]/div[3]/button[2]").click()
            time.sleep(1)
            bot.find_element_by_id("shipping-discount-selection").click()
            time.sleep(1)
            bot.find_element_by_xpath("/html/body/main/div[2]/form/div[3]/div[2]/div/div/div[3]/div/div[2]/div[1]/div").click()
            time.sleep(1)
            bot.find_element_by_xpath("/html/body/main/div[2]/form/div[4]/button[2]").click()
            time.sleep(1)
            """
        except Exception as ex:
            time.sleep(5)


ed = Posh("lam_phoebe", "_Ltc66413299")
ed.login()
ed.auto_offer("https://poshmark.com/listing/NEW-iPhone-MaxXRXXS8Plus-Glossy-Heart-case-5dc3c1f475bd8e470a64b84d")
ed.auto_offer("https://poshmark.com/listing/NEW-iPhone-XSX78Plus-Luxury-Marble-case-5dc3c1e56e32391e5c9eac1b")
ed.auto_offer("https://poshmark.com/listing/NEW-iPhone-11ProMaxXR8Plus-Electroplated-case-5dc3c1d0582af88468e52cbe")
ed.auto_offer("https://poshmark.com/listing/NEW-iPhone-MaxXRXXS78Plus-Flower-W-Holder-5dc3c1c65b565faf76ca4868")
ed.auto_offer("https://poshmark.com/listing/NEW-iPhone-11ProMaxXRXS78Plus-Cactus-case-5dc3c1ba40744ab05c706333")
ed.auto_offer("https://poshmark.com/listing/NEW-iPhone-MaxXRXXS8Plus-Heart-iPhone-case-5dc3c1a4dc11f3ecb42c40fb")
ed.auto_offer("https://poshmark.com/listing/NEW-iPhone-XXS78Plus-Plain-FullCover-case-5dc3c18d419501f3cf1d0b44")
ed.auto_offer("https://poshmark.com/listing/NEW-iPhone-MaxXRXXS78Plus-Glossy-Marble-case-5dc3b7ab4d03a040a5f71386")
ed.auto_offer("https://poshmark.com/listing/NEW-iPhone-XXS77Plus-Galaxy-Hard-Case-5dc3b7973072eef1e6443212")
ed.auto_offer("https://poshmark.com/listing/NEW-iPhone-XXS78Plus-Glossy-Planet-case-5dc3b78a993a0ddbe1d833f7")
ed.auto_offer("https://poshmark.com/listing/NEW-iPhone-XXS78Plus-Glossy-Moon-case-5dc3b77b74af4710166aa719")
ed.auto_offer("https://poshmark.com/listing/NEW-iPhone-XXS7878-Glossy-Galaxy-Sky-case-5dc3b76a60ff85f236ea1d0a")
ed.auto_offer("https://poshmark.com/listing/NEW-iPhone-XXS7878-Glossy-Night-Star-case-5dc3b75f4776df7a18e8d147")
ed.auto_offer("https://poshmark.com/listing/Urban-Outfitters-Teddy-Bear-Crop-Long-Tee-5dc65db0264a555316abf130")
ed.auto_offer("https://poshmark.com/listing/NEW-iPhone-11ProMaxXRXS78Plus-Funny-case-5dc3b73280afe19e6baa1480")
ed.auto_offer("https://poshmark.com/listing/NEW-iPhone-11ProMaxXRXS78Plus-Marble-case-5dc3b7181445650514546017")
ed.auto_offer("https://poshmark.com/listing/Accessories-NEW-iPhone-MaxXRXX-3D-Heart-case-5dc3b70cafc28242e551f0ed")
ed.auto_offer("https://poshmark.com/listing/NWOT-wave-edge-business-causal-black-dress-5dc64696d400084be558af0f")
ed.auto_offer("https://poshmark.com/listing/NEW-X7878-Dream-Conch-Shell-iPhone-case-5dc3b6e0993a0dea50d81b29")
ed.auto_offer("https://poshmark.com/listing/NEW-iPhone-MaxXRXXS78Plus-Marble-W-Holder-c-5dc3b2ad1af1ebc8171065b5")
ed.auto_offer("https://poshmark.com/listing/NEW-iPhone-MaxXRXXS78Plus-Conch-Shell-case-5dc3b29d8ecb5d986f80d309")
ed.auto_offer("https://poshmark.com/listing/Baseus-LCD-Display-Wireless-Charger-Pad-5dc3b28ef32a08f18ec0af63")
ed.auto_offer("https://poshmark.com/listing/NEW-iPhone-MaxXRXXS78Plus-Marble-W-Holder-5dc3b284648df2c05be5eb20")
ed.auto_offer("https://poshmark.com/listing/NEW-iPhone-MaxXRXXS78Plus-Dream-W-Holder-5dc3b27a86a6045964f4be28")
ed.auto_offer("https://poshmark.com/listing/NEW-iPhone-XXS7878-Glossy-Purple-Sky-case-5dc3b26eb38f0a3df448dc7b")
ed.auto_offer("https://poshmark.com/listing/NEW-iPhone-MaxXRXXS78Plus-Marble-W-Holder-5dc3b2646a044e21e1c2ca3d")
ed.auto_offer("https://poshmark.com/listing/NEW-iPhone-XXS78Plus-Glossy-Marble-case-5dc3b2445c6381eae5f3b2e2")
ed.auto_offer("https://poshmark.com/listing/NEW-iPhone-XXS7878-Glossy-iPhone-Case-5dc3b239151ccd057f2cd60e")
ed.auto_offer("https://poshmark.com/listing/NEW-iPhone-XXS78Plus-Slicon-Ring-case-5dc3b22c75bd8ecb58629285")
ed.auto_offer("https://poshmark.com/listing/NEW-iPhone-X-iPhone-XS-Cute-Pug-iPhone-case-5dc3b21d16be7054a584cd6b")
ed.auto_offer("https://poshmark.com/listing/NEW-iPhone-11ProMaxXRXS78Plus-Glossy-case-5dc3b20e62e9d58f68a15e24")
ed.auto_offer("https://poshmark.com/listing/NEW-iPhone-MaxXRXXS78Plus-Marble-W-Holder-5dc3b204eeb52374a27dc46e")
ed.auto_offer("https://poshmark.com/listing/NEW-iPhone-X-iPhone-XS-Colorful-Fish-Scale-case-5dc3bb149bb89f4d0988794f")
ed.auto_offer("https://poshmark.com/listing/NEW-iPhone-MaxXRXXS78Plus-Marble-case-5dc3bb25151ccd0ffd2e2a1c")
ed.auto_offer("https://poshmark.com/listing/NEW-iPhone-7-iPhone-8-Cherry-Blossom-Hard-case-5dc3bb3495676b551589243e")
ed.auto_offer("https://poshmark.com/listing/NEW-iPhone-MaxXRXXS78Plus-Dream-Pink-case-5dc3bb3d86a6044fa8f607af")
ed.auto_offer("https://poshmark.com/listing/NEW-iPhone-11ProMaxXRXS8Plus-Laser-Moon-Case-5dc3bb4b5b565f30bec98565")
ed.auto_offer("https://poshmark.com/listing/NEW-iPhone-XXS78Plus-Gradual-Color-Sky-case-5dc3bb5aa1f56fd1d8af033f")
ed.auto_offer("https://poshmark.com/listing/NEW-iPhone-11ProMaxXR78Plus-case-5dc3bb69afc2823e1b528b67")
ed.auto_offer("https://poshmark.com/listing/NEW-iPhone-11ProMaxXR8Plus-Electroplate-case-5dc3bb715b565faf76c989f3")
ed.auto_offer("https://poshmark.com/listing/NEW-iPhone-XXS7878-Castle-iPhone-case-5dc3bb798e2a835dbf951be9")
ed.auto_offer("https://poshmark.com/listing/NEW-iPhone-11ProMaxXRXS78Plus-Star-case-5dc3bb8a16be702872863421")
ed.auto_offer("https://poshmark.com/listing/NEW-iPhone-MaxXRXXS78Plus-Glossy-iPhone-case-5dc3bb994d03a01bd8f799d5")
ed.auto_offer("https://poshmark.com/listing/NEW-iPhone-MaxXRXXS78Plus-Glossy-Planet-case-5dc3bba886a604e0b6f614e7")
ed.auto_offer("https://poshmark.com/listing/NEW-iPhone-MaxXRXXS78Plus-Plants-Leaves-case-5dc3bbb68e2a8343b59523ae")
ed.auto_offer("https://poshmark.com/listing/NEW-iPhone-MaxXRXXS78-Floral-case-5dc3bbd2ef8d49b5de6ec088")
ed.auto_offer("https://poshmark.com/listing/NEW-iPhone-MaxXRXXS78Plus-Candy-Color-case-5dc3bbf160ff853bb1eab7c1")
ed.auto_offer("https://poshmark.com/listing/NEW-iPhone-MaxXRXXS78Plus-Glossy-Planet-case-5dc3bc03cfb5fc07ba2d197c")
ed.auto_offer("https://poshmark.com/listing/NEW-iPhone-XXS78Plus-Glossy-Lattice-Laser-Case-5dc3bc13648df2c5b5e754de")
ed.auto_offer("https://poshmark.com/listing/NEW-iPhone-XXS78Plus-Glass-Back-Cover-case-5dc3bc28993a0d7ea4d8d3e6")
ed.auto_offer("https://poshmark.com/listing/NEW-iPhone-XXS7878-Glossy-Gradient-case-5dc3bc32dce032a38b9ad439")
ed.auto_offer("https://poshmark.com/listing/NEW-iPhone-MaxXRXXS78Plus-Laser-Leopard-case-5dc3bc42ab2017b39ee07667")
ed.auto_offer("https://poshmark.com/listing/NEW-iPhone-MaxXRXXSPlus-Transparent-Rose-case-5dc3bc5080afe185c3aac737")
ed.auto_offer("https://poshmark.com/listing/NEW-iPhone-MaxXRXXS78Plus-Floral-case-5dc3bc5f7aad52ffc1b3ec0e")
ed.auto_offer("https://poshmark.com/listing/LAST-ONE-7878-iPhone-BeCool-Letter-case-5dc3bc6b0c5e3b02930e7410")
ed.auto_offer("https://poshmark.com/listing/NEW-iPhone-11ProMaxXRXS8Plus-Pineapple-case-5dc3bc87bf5430630f8cf565")
ed.auto_offer("https://poshmark.com/listing/NEW-iPhone-XXS7878-Marble-Slicon-Ring-case-5dc3bc99bf54308e5d8cf78f")
ed.auto_offer("https://poshmark.com/listing/NEW-iPhone-MaxXRXXS78Plus-Marble-W-Holder-5dc3bca1510bca31b375320b")
ed.auto_offer("https://poshmark.com/listing/NEW-iPhone-MaxXRXXS78Plus-Marble-W-Holder-5dc3bcac3b99851532bb16ef")
ed.auto_offer("https://poshmark.com/listing/Baseus-Magnetic-Cable-Holder-Desktop-5dc3bcb8ba97fe888878b1e1")
ed.auto_offer("https://poshmark.com/listing/NEW-4-Color-Exquisite-Simple-Women-Leather-Watch-5dc3bcc8ef8d49bc8a6edeea")
ed.auto_offer("https://poshmark.com/listing/NEW-iPhone-11ProMaxXR78Plus-Gold-Leaves-case-5dc3bcedcdbd4903ec390187")
ed.auto_offer("https://poshmark.com/listing/NEW-iPhone-MaxXRXXS78-Glossy-Geometric-case-5dc3bcfd65d17f6c1a2b7823")
ed.auto_offer("https://poshmark.com/listing/NEW-iPhone-MaxXRXXS78Plus-Floral-case-5dc3bd0b6ce3ccd7f42aa523")
ed.auto_offer("https://poshmark.com/listing/NEW-iPhone-XXS78Plus-PlaidDaisy-Pink-case-5dc3bd16574bd502c38dcf29")
ed.auto_offer("https://poshmark.com/listing/NEW-iPhone-MaxXRXXS78Plus-Stardust-Case-5dc3bd2653f5e7112090f3f3")
ed.auto_offer("https://poshmark.com/listing/NEW-iPhone-MaxXRXXS78-Glossy-Cat-case-5dc3bd47419501952e1c8e8a")
ed.auto_offer("https://poshmark.com/listing/NEW-iPhone-MaxXRXXS78Plus-Conch-Shell-case-5dc3bd5640744ae17e6fdfae")
ed.auto_offer("https://poshmark.com/listing/NEW-iPhone-MaxXRXXS78Plus-Moon-case-5dc3bd685b565ffe80c9c83e")
ed.auto_offer("https://poshmark.com/listing/NEW-iPhone-XXS78Plus-Planet-iPhone-case-5dc3bd7a75bd8e01ff64340e")
ed.auto_offer("https://poshmark.com/listing/NEW-iPhone-XSX78Plus-Aurora-Laser-Marble-case-5dc3bd853f79ea5ff3b6c367")
ed.auto_offer("https://poshmark.com/listing/NEW-iPhone-XXS78Plus-Dream-Glossy-Marble-case-5dc3bd906e3239d2859e2b97")
ed.auto_offer("https://poshmark.com/listing/NEW-iPhone-X-iPhone-XS-Aurora-Laser-Stripe-case-5dc3bd9fef8d4990cd6ef926")
ed.auto_offer("https://poshmark.com/listing/NEW-iPhone-MaxXRXXS78Plus-Glossy-Marble-case-5dc3bdb250177f3644c4e253")
ed.auto_offer("https://poshmark.com/listing/NEW-iPhone-MaxXRXXS78Plus-Star-case-5dc3bdce8e2a83eec19567cc")
ed.auto_offer("https://poshmark.com/listing/NEW-iPhone-XSX78Plus-Aurora-Laser-case-5dc3bdee151ccd6c882e85b9")
ed.auto_offer("https://poshmark.com/listing/NEW-iPhone-MaxXRXXS78Plus-W-Holder-5dc3bdffacb24bbbd0a8c930")
ed.auto_offer("https://poshmark.com/listing/NEW-iPhone-XSX78Plus-Star-Glitter-Powder-case-5dc3be0a993a0d7dbdd9125b")
ed.auto_offer("https://poshmark.com/listing/NEW-iPhone-MaxXRXXS78Plus-Moon-Case-5dc3be1b01e20432c2863a51")
ed.auto_offer("https://poshmark.com/listing/NEW-iPhone-XSX78Plus-Aurora-Universe-case-5dc3be2bc2835c8f9cc5f459")
ed.auto_offer("https://poshmark.com/listing/NEW-iPhone-MaxXRXXS78Plus-Electroplated-case-5dc3be3ebbce0be559fe6771")
ed.auto_offer("https://poshmark.com/listing/NEW-iPhone-XXS7878-Shell-iPhone-case-5dc3be4d5b565f1a54c9e37b")
ed.auto_offer("https://poshmark.com/listing/NEW-iPhone-XXS78Plus-Retro-Moon-iPhone-case-5dc3be5bcfd1242ee440212f")
ed.auto_offer("https://poshmark.com/listing/NEW-iPhone-MaxXRXSX78Plus-Aurora-Moon-case-5dc3be6da1f56fd01faf673c")
ed.auto_offer("https://poshmark.com/listing/NEW-iPhone-66SXXS7878-Moon-Black-Cat-Case-5dc3be7b16be70cfcb8692a8")
ed.auto_offer("https://poshmark.com/listing/NEW-iPhone-XXS7878-Glossy-Moon-case-5dc3be88befd3e1f928bf68f")
ed.auto_offer("https://poshmark.com/listing/NEW-iPhone-XSX78Plus-White-Marble-case-5dc3be9a993a0db8e3d922d3")
ed.auto_offer("https://poshmark.com/listing/NEW-iPhone-MaxXRXXS78Plus-Glossy-Heart-case-5dc3beac1af1eb0558121ac8")
ed.auto_offer("https://poshmark.com/listing/NEW-iPhone-XXS78Plus-Candy-AntiKnock-case-5dc3bebfb38f0aefbb4a9957")
ed.auto_offer("https://poshmark.com/listing/NEW-iPhone-11ProMaxXRXS78Plus-Marble-case-5dc3bed0f51dbfaf4f21847f")
ed.auto_offer("https://poshmark.com/listing/NEW-NEW-iPhone-MaxXRXXS8Plus-Letter-case-5dc3bee116be70cc48869dda")
ed.auto_offer("https://poshmark.com/listing/New-iPhone-XXS78Plus-Shining-Heart-Phone-case-5dc3beecb81fca6c1bec9271")
ed.auto_offer("https://poshmark.com/listing/NEW-iPhone-XSX78Plus-Aurora-Laser-Marble-case-5dc3bef93f79ea6ab8b6ef8f")
ed.auto_offer("https://poshmark.com/listing/LAST-ONE-NEW-iPhone-X-iPhone-XS-3D-Cloud-case-5dc3bf08b81fca0e5aec95a9")
ed.auto_offer("https://poshmark.com/listing/NEW-iPhone-MaxXRXXS78Plus-Marble-W-Holder-5dc3bf1786a604b3e0f67e61")
ed.auto_offer("https://poshmark.com/listing/NEW-iPhone-MaxXRXXS78-Mirror-AntiKnock-case-5dc3bf227aad5239d2b4400a")
ed.auto_offer("https://poshmark.com/listing/NEW-iPhone-MaxXRXXS78-Glossy-Geometric-case-5dc3bf301af1eb3913122a51")
ed.auto_offer("https://poshmark.com/listing/NEW-iPhone-MaxXRXXS78-Mirror-AntiKnock-case-5dc3bf385b565feddbc9fe21")
ed.auto_offer("https://poshmark.com/listing/NEW-iPhone-MaxXRXXS78Plus-Marble-W-Holder-5dc3bf4c5263ec66ca4431fc")
ed.auto_offer("https://poshmark.com/listing/NEW-Unisex-Creative-Design-Leather-Watch-5dc3bf6fc2835ccacec619d8")
ed.auto_offer("https://poshmark.com/listing/NEW-iPhone-MaxXRXXS78Plus-Floral-case-5dc3bf7ca1f56f5548af865c")
ed.auto_offer("https://poshmark.com/listing/NEW-iPhone-XXS78Plus-Glossy-heart-case-5dc3bf88a16f973656c4b8b8")
ed.auto_offer("https://poshmark.com/listing/NEW-iPhone-MaxXRXXS78Plus-3D-heart-case-5dc3bf99eeb523c64a7fb58f")
ed.auto_offer("https://poshmark.com/listing/NEW-iPhone-XXS7878-iPhone-Glossy-case-5dc3bfab0c5e3bc3a40ed793")
ed.auto_offer("https://poshmark.com/listing/NEW-iPhone-MaxXRXXS78-Mirror-Fullcover-case-5dc3bfbc8e881ee421e2e3e4")
ed.auto_offer("https://poshmark.com/listing/NEW-iPhone-MaxXRXXS78Plus-Glossy-heart-case-5dc3bfcd7bc360173f041221")
ed.auto_offer("https://poshmark.com/listing/NEW-iPhone-7-Plus-8-Plus-Glitter-Powder-case-5dc3bfdf62e9d57683a35059")
ed.auto_offer("https://poshmark.com/listing/NEW-iPhone-7788-Glossy-Moon-case-5dc3bfeca1f56f3e76af9354")
ed.auto_offer("https://poshmark.com/listing/NEW-iPhone-MaxXRXXS78Plus-Glossy-Planet-Case-5dc3bffe53f5e7df959149ef")
ed.auto_offer("https://poshmark.com/listing/Brown-puffer-jacket-5dc3b72aa16f97605bc3a415")
ed.auto_offer("https://poshmark.com/listing/iPhone-7878-Glossy-Planet-Universe-case-5dc3c01053f5e76e8e914bf5")
ed.auto_offer("https://poshmark.com/listing/NEW-iPhone-MaxXRXXS78Plus-3D-Heart-case-5dc3c02474af4769e76bc65e")
ed.auto_offer("https://poshmark.com/listing/NEW-iPhone-11ProMaxXR8Plus-Glitter-Star-case-5dc3c02e4776df5184e9f265")
ed.auto_offer("https://poshmark.com/listing/NEW-iPhone-XXS7878-Slicon-Ring-case-5dc3c039574bd5f4d38e31df")
ed.auto_offer("https://poshmark.com/listing/NEW-iPhone-11ProMaxXRXS78P-Marble-W-Holder-5dc3c04dafc282d2d7532138")
ed.auto_offer("https://poshmark.com/listing/NEW-iPhone-XXS7878-Marble-Slicon-Ring-case-5dc3c05fa16f97f7a2c4d1d1")
ed.auto_offer("https://poshmark.com/listing/NEW-iPhone-XXS78Plus-Dream-Shell-Case-5dc3c06b6e3239f1899e825f")
ed.auto_offer("https://poshmark.com/listing/NEW-iPhone-MaxXRXXS78Plus-Marble-W-Holder-5dc3c07b3b9985b8e6bb8ca1")
ed.auto_offer("https://poshmark.com/listing/NEW-iPhone-MaxXRXXS78Plus-Marble-W-Holder-5dc3c08765d17f86c02be337")
ed.auto_offer("https://poshmark.com/listing/NEW-iPhone-XSX78Plus-Aurora-Laser-Marble-case-5dc3c09201e2046c46868851")
ed.auto_offer("https://poshmark.com/listing/NEW-iPhone-MaxXRXXS8Plus-Mirror-case-5dc3c0a03ce2411b822cae9f")
ed.auto_offer("https://poshmark.com/listing/NEW-7878-iPhone-Dream-Marble-case-5dc3c0b274af4778576bd6dc")
ed.auto_offer("https://poshmark.com/listing/NEW-iPhone-MaxXRXXS78Plus-3D-Heart-case-5dc3c0c33072ee1a5b455ee5")
ed.auto_offer("https://poshmark.com/listing/NEW-iPhone-MaxXRXXS78Plus-Glossy-heart-case-5dc3c0e0ab2017635be102ff")
ed.auto_offer("https://poshmark.com/listing/NEW-iPhone-MaxXRXXS78Plus-3D-Heart-case-5dc3c0f2bbce0bd96ffeb7bd")
ed.auto_offer("https://poshmark.com/listing/NEW-iPhone-XSX78Plus-Matt-Letter-Hard-case-5dc3c102eeb5239f6d7fe037")
ed.auto_offer("https://poshmark.com/listing/NEW-iPhone-11ProMaxXRXS78Plus-Marble-case-5dc3c11401e204922a869768")
ed.auto_offer("https://poshmark.com/listing/NEW-iPhone-XSX78Plus-Glossy-Feather-case-5dc3c1277bc36018fb043970")
ed.auto_offer("https://poshmark.com/listing/NEW-iPhone-MaxXRXXS8Plus-Aurora-Laser-case-5dc3c13ef2d35ed008f077e3")
ed.auto_offer("https://poshmark.com/listing/NEW-iPhone-MaxXRXXS78Plus-Aurora-Laser-case-5dc3c14fba97fea7bb793be6")
ed.auto_offer("https://poshmark.com/listing/NEW-iPhone-XXS78Plus-Glossy-Dot-Big-case-5dc3c15fbf5430630f8d87a6")
ed.auto_offer("https://poshmark.com/listing/NEW-iPhone-XXS7878-Electroplate-case-5dc3c16d3b99853797bba829")
ed.auto_offer("https://poshmark.com/listing/NEW-iPhone-XXS7878-Glossy-Heart-Case-5dc3c17dc2835c8439c65764")
ed.auto_offer("https://poshmark.com/listing/NEW-iPhone-MaxXRXXS78Plus-Floral-case-5dc3c1d8151ccda2aa2ef6d5")
ed.auto_offer("https://poshmark.com/listing/NEW-iPhone-11ProMaxXRXS78P-Marble-W-Holder-5dc3c3a774af47a1e16c2855")
ed.auto_offer("https://poshmark.com/listing/NEW-iPhone-11ProMaxXR78Plus-Retro-case-5dc3c39865d17fb11f2c361e")
ed.auto_offer("https://poshmark.com/listing/NEW-iPhone-MaxXRXXS78Plus-Dream-Shell-case-5dc3c3899bb89f84a1897792")
ed.auto_offer("https://poshmark.com/listing/NEW-iPhone-11ProMaxXRXS78Plus-Planet-case-5dc3c37a464c9f071188266c")
ed.auto_offer("https://poshmark.com/listing/NEW-LAST-ONE-Unisex-Casual-Marble-Watch-5dc3c36040744aa632708fbf")
ed.auto_offer("https://poshmark.com/listing/NEW-iPhone-XXS78Plus-Glossy-Big-Dot-case-5dc3c3362c6fc648604e5be6")
ed.auto_offer("https://poshmark.com/listing/NEW-iPhone-XXS78Plus-Glossy-Rocket-case-5dc3c34674af4719876c1ddc")
ed.auto_offer("https://poshmark.com/listing/NEW-LAST-ONE-Unisex-Creative-Design-Watch-5dc3c35108fc577a853736bd")
ed.auto_offer("https://poshmark.com/listing/NEW-iPhone-XXS78Plus-Black-Conch-Shell-case-5dc3c20e9495d23a83964ff3")
ed.auto_offer("https://poshmark.com/listing/NEW-Moon-Stars-Dial-Casual-Fashion-quartz-watches-5dc3c21b2c6fc6675d4e3e60")
ed.auto_offer("https://poshmark.com/listing/NEW-iPhone-MaxXRXXS78Plus-Gradual-Case-5dc3c2283f79ea996eb748f0")
ed.auto_offer("https://poshmark.com/listing/NEW-iPhone-XXS7878-Dream-Paint-case-5dc3c23174af4745236c0162")
ed.auto_offer("https://poshmark.com/listing/NEW-Cute-AirPods-Soft-Silicone-Case-5dc3c2556a044e77acc4efc1")
ed.auto_offer("https://poshmark.com/listing/NEW-XXS7878-iPhone-Silicon-Ring-case-5dc3c2603ce241f69c2ce173")
ed.auto_offer("https://poshmark.com/listing/NEW-iPhone-7-iPhone-8-Pink-Shining-Leather-case-5dc3c2813a4dc24094e4b405")
ed.auto_offer("https://poshmark.com/listing/NEW-7878-iPhone-Glossy-Blue-Marble-case-5dc3c29379d968b031a8f5c6")
ed.auto_offer("https://poshmark.com/listing/NEW-iPhone-XXS78Plus-Rose-Flower-case-5dc3c29f86a6045009f6e193")
ed.auto_offer("https://poshmark.com/listing/NEW-iPhone-XSX78Plus-Big-Dot-Transparent-Case-5dc3c2afe377533014805278")
ed.auto_offer("https://poshmark.com/listing/NEW-iPhone-MaxXRXXS78Plus-Transparent-case-5dc3c2bbb81fcac5fbed01e8")
ed.auto_offer("https://poshmark.com/listing/NEW-iPhone-MaxXRXXS78-Transparent-case-5dc3c2cbef8d495d2c6f8c26")
ed.auto_offer("https://poshmark.com/listing/NEW-iPhone-XXS7878-Glossy-Dream-case-5dc3c2db4776dfc237ea3d7d")
ed.auto_offer("https://poshmark.com/listing/NEW-iPhone-XXS78-Glossy-Diamond-case-5dc3c2eb8e881e914ce33c90")
ed.auto_offer("https://poshmark.com/listing/NEW-iPhone-11ProMaxXRXS78Plus-case-5dc3c2f74776df4c0eea4046")
ed.auto_offer("https://poshmark.com/listing/NEW-iPhone-XXS7788-3D-Heart-iPhone-case-5dc3c308cdbd49abad39b454")
ed.auto_offer("https://poshmark.com/listing/NEW-iPhone-11ProMaxXRXS78P-Marble-W-Holder-5dc3c313bbce0bc765feefa8")
ed.auto_offer("https://poshmark.com/listing/NEW-iPhone-XXS78Plus-Glossy-Universe-case-5dc3c32a7aad528a34b4b148")
ed.auto_offer("https://poshmark.com/listing/NEW-4-Color-Simple-Bracelet-Watch-5dc3c31c74af479b456c198d")
ed.auto_offer("https://poshmark.com/listing/NWT-Nine-West-beanie-5dc3c279eeb523aaff80089a")
ed.auto_offer("https://poshmark.com/listing/Removable-Jean-Midi-Dress-5dc3c26fdc11f3f2612c56b4")
ed.auto_offer("https://poshmark.com/listing/NEW-One-set-Summer-Mesh-Tee-and-Tank-Dress-5dc3c24165d17f4caf2c1404")
ed.auto_offer("https://poshmark.com/listing/Timberlands-Kid-sweater-5dc3c205574bd5a2288e651d")
ed.auto_offer("https://poshmark.com/listing/Urban-Outfitters-White-Y-neck-Romper-5dc3ba4f9bb89f95ba885feb")
ed.auto_offer("https://poshmark.com/listing/NEW-iPhone-MaxXRXXS8Plus-Crystal-w-holder-5dc3b255aa730993ce4448c3")
ed.auto_offer("https://poshmark.com/listing/NEW-iPhone-7878-Glossy-Universe-case-5dc3bdc3648df25a8de78de3")
ed.auto_offer("https://poshmark.com/listing/NEW-iPhone-11ProMaxXRXS78-Marble-W-Holder-5dc3b7bb6ce3ccb5ed29f15b")
ed.auto_offer("https://poshmark.com/listing/NEW-iPhone-MaxXRXXS78Plus-Shell-Ring-Holder-5dc3b7c579d9683ecfa79fa7")
ed.auto_offer("https://poshmark.com/listing/NEW-iPhone-X7878-3D-Heart-Flower-case-5dc3b7d4eeb5239a107eb50f")
ed.auto_offer("https://poshmark.com/listing/NEW-iPhone-MaxXRXXS78Plus-Floral-case-5dc3b7f23f79ea0de2b6082d")
ed.auto_offer("https://poshmark.com/listing/NEW-iPhone-XSX78Plus-Aurora-Laser-Floral-case-5dc3b7ff648df24306e6c9e9")
ed.auto_offer("https://poshmark.com/listing/NEW-iPhone-XXS78Plus-Glossy-Gold-Big-Dot-case-5dc3b80ea1f56ffa04ae91ce")
ed.auto_offer("https://poshmark.com/listing/NEW-iPhone-7878-Conch-Shell-case-5dc3b81fcfd1240a8e3f5490")
ed.auto_offer("https://poshmark.com/listing/NEW-Shiny-AirPods-Soft-Silicone-Case-5dc3b82e1445657da0548994")
ed.auto_offer("https://poshmark.com/listing/NEW-iPhone-XSX78Plus-Aurora-GLASS-Deer-case-5dc3b83e16be70ff7a85c0d6")
ed.auto_offer("https://poshmark.com/listing/NEW-iPhone-78Plus-Glossy-Diamond-iPhone-case-5dc3b84d510bca305e74a16d")
ed.auto_offer("https://poshmark.com/listing/NEW-iPhone-MaxXRXXS78Plus-Marble-W-Holder-5dc3b85adce032fb579a53fb")
ed.auto_offer("https://poshmark.com/listing/NEW-Plating-AirPods-Hard-Case-with-Hook-5dc3b864afc2820f7e52231b")
ed.auto_offer("https://poshmark.com/listing/NEW-iPhone-11ProMaxXR8Plus-Electroplated-case-5dc3b8749495d279b2951fbe")
ed.auto_offer("https://poshmark.com/listing/NEW-4-Color-Simple-Bracelet-Watch-5dc3b87f9bb89f2b2588215e")
ed.auto_offer("https://poshmark.com/listing/NEW-iPhone-XXS78Plus-Glossy-Marble-case-5dc3b88fcfaad2a500a0279c")
ed.auto_offer("https://poshmark.com/listing/NEW-iPhone-MaxXRXXS78Plus-Jade-Marble-case-5dc3b897aa730949e6454150")
ed.auto_offer("https://poshmark.com/listing/NEW-iPhone-11ProMaxXR8Plus-Electroplated-case-5dc3b8a3648df29f36e6e170")
ed.auto_offer("https://poshmark.com/listing/NEW-iPhone-MaxXRXXS78Plus-Gradual-Case-5dc3b8abcfd124264b3f67ca")
ed.auto_offer("https://poshmark.com/listing/NEW-iPhone-MaxXRXXS78Plus-Shell-W-Holder-5dc3b8b475bd8e7ccd6393b9")
ed.auto_offer("https://poshmark.com/listing/NEW-iPhone-11ProMaxXRXS78Plus-Art-case-5dc3b8c150177f7703c43eb0")
ed.auto_offer("https://poshmark.com/listing/NEW-iPhone-MaxXRXXS8Plus-Rainbow-Effect-case-5dc3b8c9f51dbfad5c20c15e")
ed.auto_offer("https://poshmark.com/listing/NEW-iPhone-MaxXRXXS8Plus-Marble-Feather-case-5dc3b8d940744a1de16f4dbf")
ed.auto_offer("https://poshmark.com/listing/NEW-iPhone-MaxXRXXS78Plus-Conch-Shell-case-5dc3b8ea79d968c4aba7c8e4")
ed.auto_offer("https://poshmark.com/listing/NEW-iPhone-MaxXRXXS78Plus-Marble-Square-case-5dc3b8f974af472efd6aded5")
ed.auto_offer("https://poshmark.com/listing/NEW-iPhone-11ProMaxXRXS78P-Marble-W-Holder-5dc3b9087aad522034b378e6")
ed.auto_offer("https://poshmark.com/listing/NEW-iPhone-MaxXRXXS78Plus-Cute-Pig-Case-5dc3b914f32a08f0b4c1b2b8")
ed.auto_offer("https://poshmark.com/listing/NEW-iPhone-MaxXRXXS78Plus-Mirror-case-5dc3b9209bb89ff575883789")
ed.auto_offer("https://poshmark.com/listing/Adidas-logo-hoodie-5dc3b9396ce3cc63e22a2733")
ed.auto_offer("https://poshmark.com/listing/NEW-iPhone-XSX78Plus-Luxury-Marble-case-5dc3b943510bcaff8e74c342")
ed.auto_offer("https://poshmark.com/listing/NEW-iPhone-XXS78Plus-Glossy-Castle-iPhone-case-5dc3c36d40744a6a607090ed")
ed.auto_offer("https://poshmark.com/listing/NEW-iPhone-MaxXRXXS78Plus-Floral-case-5dc3bf59a16f97f778c4b2f2")
ed.auto_offer("https://poshmark.com/listing/HOST-PICK-6242017-Tommy-Hilfiger-Sweater-5dc3b74bef8d4994ca6e22c7")
ed.auto_offer("https://poshmark.com/listing/Music-Pattern-high-rise-Jean-short-5dc3bde23a4dc2f594e42dd6")
ed.auto_offer("https://poshmark.com/listing/Thick-Warm-UW-Huskies-Hoodie-5dc649ab79df27d0e27d9f19")
ed.auto_offer("https://poshmark.com/listing/NEW-iPhone-MaxXRXXS8Plus-Crystal-w-holder-5dc3baf0e25b327186b30a70")
ed.auto_offer("https://poshmark.com/listing/NEW-iPhone-11ProMaxXRXS8Plus-Pineapple-case-5dc3bae67bc360b88e037891")
ed.auto_offer("https://poshmark.com/listing/NEW-iPhone-11ProMaxXRXS78P-Marble-W-Holder-5dc3badcb38f0a65ac4a213f")
ed.auto_offer("https://poshmark.com/listing/NEW-iPhone-XXS78-Glossy-Cloud-Purple-case-5dc3bacd4d03a0d65bf77fd4")
ed.auto_offer("https://poshmark.com/listing/NEW-iPhone-XSX78Plus-Aurora-Sunflower-case-5dc3babd993a0daf66d8a4f9")
ed.auto_offer("https://poshmark.com/listing/NEW-iPhone-MaxXRXXS78Plus-Floral-case-5dc3bab2e3775307827f60c0")
ed.auto_offer("https://poshmark.com/listing/NEW-iPhone-MaxXRXXS78Plus-Pig-W-Holder-5dc3baa5cdbd49d21338b7f5")
ed.auto_offer("https://poshmark.com/listing/NEW-7878-Glossy-Pink-Marble-Soft-case-5dc3ba9cacb24b0157a859f7")
ed.auto_offer("https://poshmark.com/listing/NEW-iPhone-XXS78Plus-Granite-Stone-Marble-case-5dc3ba8a86a604ca08f5f1b9")
ed.auto_offer("https://poshmark.com/listing/NEW-iPhone-MaxXRXXS78Plus-Floral-case-5dc3ba7f105293437d775c7a")
ed.auto_offer("https://poshmark.com/listing/NEW-iPhone-MaxXRXXS78Plus-Floral-case-5dc3ba731af1ebb916119263")
ed.auto_offer("https://poshmark.com/listing/NEW-iPhone-MaxXRXXS78Plus-Floral-case-5dc3ba675263ec7a45439605")
ed.auto_offer("https://poshmark.com/listing/NEW-Samsung-Type-C-LED-Light-Fast-Charger-Cable-5dc3ba5879d968518da7fa83")
ed.auto_offer("https://poshmark.com/listing/NEW-XXS7878-iPhone-Silicon-Marble-Ring-case-5dc3ba45105293da1a7754e1")
ed.auto_offer("https://poshmark.com/listing/NEW-iPhone-11ProMaxXRXS78Plus-Vintage-case-5dc3ba36b502819ec89a8320")
ed.auto_offer("https://poshmark.com/listing/NEW-Spider-Cute-AirPods-Soft-Silicone-Case-5dc3ba2dbbce0b33e0fde53b")
ed.auto_offer("https://poshmark.com/listing/NEW-iPhone-7-iPhone-8-Glossy-Geometric-Case-5dc3ba227bc3608dc2035f36")
ed.auto_offer("https://poshmark.com/listing/NEW-iPhone-XXS7878-Laser-Mirror-case-5dc3ba10ef8d4988bf6e8770")
ed.auto_offer("https://poshmark.com/listing/NEW-iPhone-MaxXRXXS78Plus-DIY-3D-case-5dc3ba016ce3ccb2f02a42bb")
ed.auto_offer("https://poshmark.com/listing/NEW-iPhone-X-iPhone-XS-Glitter-Powder-case-5dc3b9ee6e323901a79db428")
ed.auto_offer("https://poshmark.com/listing/NEW-iPhone-MaxXRXXS78Plus-Pineapple-case-5dc3b9e24776df701ce92e22")
ed.auto_offer("https://poshmark.com/listing/NEW-iPhone-MaxXRXXS78Plus-Mirror-W-Holder-5dc3b9d63072ee23ef44856f")
ed.auto_offer("https://poshmark.com/listing/NEW-iPhone-XXS7878-Slicon-Ring-case-5dc3b9cc0c5e3b5a810e1d6d")
ed.auto_offer("https://poshmark.com/listing/NEW-Small-Dial-simple-Glitter-Leather-Watch-5dc3b9bf648df22d56e7086c")
ed.auto_offer("https://poshmark.com/listing/NEW-iPhone-11ProMax-Silicone-Solid-Candy-case-5dc3b9b4dc11f37b8d2b4b9b")
ed.auto_offer("https://poshmark.com/listing/NEW-iPhone-11ProMax-Shockproof-Geometric-case-5dc3b9a4144565286b54bd9d")
ed.auto_offer("https://poshmark.com/listing/NEW-iPhone-MaxXRXXS78-Crystalline-Marble-case-5dc3b98e08fc57a5ce360ec8")
ed.auto_offer("https://poshmark.com/listing/NEW-Bubble-Tea-AirPods-Soft-Silicone-Case-5dc3b9804d03a08844f753c0")
ed.auto_offer("https://poshmark.com/listing/NEW-4-Color-Simple-Bracelet-Watch-5dc3b9721052930c457737ea")
ed.auto_offer("https://poshmark.com/listing/NEW-iPhone-7-iPhone-8-Zebra-Painting-case-5dc3b962ab201771bee016bb")
ed.auto_offer("https://poshmark.com/listing/NEW-iPhone-11ProMaxXRXS78Plus-Marble-case-5dc3b954acb24b20b2a82e83")
ed.auto_offer("https://poshmark.com/listing/NEW-7878-Conch-Shell-Phone-Case-5dc3b6fd151ccd38502d96f8")
ed.auto_offer("")
ed.auto_offer("")
ed.auto_offer("")
ed.auto_offer("")
ed.auto_offer("")
ed.auto_offer("")
ed.auto_offer("")
ed.auto_offer("")
ed.auto_offer("")
ed.auto_offer("")
ed.auto_offer("")
ed.auto_offer("")
ed.auto_offer("")
ed.auto_offer("")
ed.auto_offer("")
ed.auto_offer("")
ed.auto_offer("")
ed.auto_offer("")
ed.auto_offer("")
ed.auto_offer("")
ed.auto_offer("")
ed.auto_offer("")
ed.auto_offer("")
ed.auto_offer("")
ed.auto_offer("")
ed.auto_offer("")

