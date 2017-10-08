import sys, datetime

d = datetime.datetime.today()
date = d.strftime("%B %d, %Y.")
#bugid = sys.argv[1]
url = sys.argv[1]

takeover = """ <title><h2 align="center">Session Takeover Vulnerability Found at """+url+"""</h2></title>
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
<p>Sessions of users accounts not terminated after been password changed.</p>
<br/>

<h3>Steps to reproduce the issue</h3>
<p>(You have to use two browsers here. You can also use Incognito mode)</p>
<ol>
<li>Register an account on """+url+""" with a valid information.</li>
<li>Logged into your account with the first browser.</li>
<li>On the second browser, Login on the same account and Change/Reset Password.</li>
<li>Now go back to the first browser and refresh the link i.e. """+url+""".</li>
<br/><p>You will notice, sessions are still alive and not getting terminated.</p>
</ol>
<br/>

<h3>Possible Impact Scenario</h3>
<p style="font-family:Times">Suppose Victim logged into his account at&nbsp;internet cafe of London. After his work, he flew back to New York and forgot to Logout. Assume bad guy seats on the same physical machine and finds victim's account open. Now somehow, victim got to know that someone is using his account, but he can't just fly back to London to stop the unusual activity. The only thing he can now do is - change his password, so that all active sessions must get terminated. But because of this vulnerability present in your application, attacker can use victims account information since all sessions are not getting terminating even after password change. This may lead to miss-use of victims details and account too.</p>

<br/>
<br/>
<br/>

<h3>Expected behaviour</h3>
<p>All live sessions must be terminate after password changed.</p>
<br/>

<h3>Related Issue</h3>
<p>https://hackerone.com/reports/119262</p>
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
pdf.write_html(takeover)
pdf.output(url+'_takeover.pdf', 'F')
