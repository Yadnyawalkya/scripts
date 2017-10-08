import sys, datetime

d = datetime.datetime.today()
date = d.strftime("%B %d, %Y.")
#bugid = sys.argv[1]
url = sys.argv[1]

hijacking = """ <title><h2 align="center">Session Hijacking Vulnerability on """+url+"""</h2></title>
<hr/>

<h3>Browser used:</h3>
<ul>
<li>Mozilla Firefox v56</li>
<li>Google Chrome v61</li>
</ul>
<br/>

<h3>Operating System Used:</h3>
<ul>
<li>Window 10</li>
<li>Ubuntu 16.04</li>
</ul>
<br/>

<h3>Login Required:</h3>
<p>Yes</p>
<br/>

<h3>Vulnerable Link:</h3>
<p>"""+url+"""</p>
<br/>

<h3>Description</h3>
<p>The Session Hijacking attack consists of the exploitation of the web session control mechanism, which is normally managed for a session token. The Session Hijacking attack compromises the session token by stealing or predicting a valid session token to gain unauthorized access to the Web Server. Once the attacker have successfully stolen the Session Token of the user, the attacker is able to log into the victim's session by using the cookies which he have stolen.</p>
<br/>

<h3>The issue</h3>
<p>So when I was testing the whole site for different web application vulnerability i have found this issue. The main cause for this attack is that the Session was still valid even if the user logs out. There are many attacks which have limited impact as if they log into the victim's account by using the victim's cookies, the session will expire when the remote user logs out but in this case the session was not expiring even if the remote user logs out. This is the issue which makes this attack more risky.</p>
<br/>

<h3>What the attacker will do once he got the session token?</h3>
<p>Once the attacker gets the Session Token of the user, he will insert those into his browser and will be able to log into the victim's account as there are no validation at the time. There must be some kind of protection that more than 1 users should not be able to use a single session. But in this case the attacker can use the session too. Once attacker gets into the account he can fully compromise the account and he can change any detail of the account as he got fully access over it.</p>
<br/>

<h3>What is Impact of vulnerability?</h3>
<p>User account compromisation and can be exploit to permanent accout takeover.</p>
<br/>

<h3>Steps to reproduce the issue</h3>
<ol>
<li>Login to your account and copy current URL</li>
<li>Copy your cookies by using 'Edit This Cookie' Chrome Extension (by Export Cookie Option)</li>
<li>Logout from account</li>
<li>Clear browser cookies</li>
<li>Paste cookies which copied in step 2 (by Import cookie option) and goto URL which
copies at step 1.</li>
<br/><p>You will find user directly logged in without any trouble !</p>
</ol>
<br/>

<h3>Possible Impact Scenario</h3>
<p>Suppose Victim Logged into his account at internet cafe and forgot to Logout. Suppose You are attacker and you found victims account is open on same PC. Now attacker can download 'EditThisCookie 1.4.1' Chrome extension and export/copy cookie of victims acc in text file. Now attacker have victims account's cookies so he can just import that cookie with 'EditThisCookie' and use victims account anytime. This may leads to miss-use of victims details and his account.</p>
<br/>

<h3>Founded on</h3>
<p>"""+date+"""</p>
<br/>

<h3>Founded by</h3>
<p>Yadnyawalkya Tale
<br/>Security Researcher,
<br/><a href="https://www.linkedin.com/in/yvtale">LinkedIn</a>
</p>

<br/>
<br/>
<p><h4><b>I'm more than happy to participate if you have bug-bounty/responsible discloser program.</b></h4>
<p>You can send direct invitation at <i>yadnyawalkyatale@gmail.com</i> email or <strong>On <b>HackerOne</b></strong>: <em>yadnyawalkya_tale</em> or <strong><b>Bugcrowd</b></strong>: <em>yadnyawalkya</em></p>.

<br/>
<br/>
<hr/>
<h2 align="center">THANK YOU!</h2>
<hr/>
"""

from fpdf import FPDF, HTMLMixin

class MyFPDF(FPDF, HTMLMixin):
    pass

pdf = MyFPDF()
#First page
pdf.add_page()
pdf.write_html(hijacking)
pdf.output(url.replace("https://","").replace("http://","")+'_hijacking.pdf', 'F')

