#!/usr/bin/env python2

SCRIPTS = [
    "jquery.min.js",
    "bootstrap.min.js",
]

CSS_PATHS = [
    "bootstrap.min.css",
    'website.css'
]

def attrs(**kw):
    for k in kw:
        assert '"' not in kw[k]

    kwstr = " ".join('{}="{}"'.format(k.strip('_'), kw[k]) for k in kw)
    return kwstr

def table(body, **kw):
    kwstr = attrs(**kw)
    return "<table {}>{}</table>".format(kwstr, body)

def tr(body, **kw):
    kwstr = attrs(**kw)
    return "<tr {}>{}</tr>".format(kwstr, body)

def td(body, **kw):
    kwstr = attrs(**kw)
    return "<td {}>{}</td>".format(kwstr, body)

def div(body, **kw):
    kwstr = attrs(**kw)
    return "<div {}>{}</div>".format(kwstr, body)

def span(body, **kw):
    kwstr = attrs(**kw)
    return "<span {}>{}</span>".format(kwstr, body)

def ol(body, **kw):
    kwstr = attrs(**kw)
    return '<ol {}>{}</ol>'.format(kwstr, body)

def ul(body, **kw):
    kwstr = attrs(**kw)
    return '<ul {}>{}</ul>'.format(kwstr, body)

def li(body, **kw):
    kwstr = attrs(**kw)
    return '<li {}>{}</li>'.format(kwstr, body)

def p(body, **kw):
    kwstr = attrs(**kw)
    return '<p {}>{}</p>'.format(kwstr, body)

def h1(body, **kw):
    kwstr = attrs(**kw)
    return '<h1 {}>{}</h1>'.format(kwstr, body)

def h2(body, **kw):
    kwstr = attrs(**kw)
    return '<h2 {}>{}</h2>'.format(kwstr, body)

def img(link, **kw):
    kwstr = attrs(**kw)
    return "<img src=\"{}\"/ {}>".format(link, kwstr)

def a(text, link, **kw):
    kwstr = attrs(**kw)
    return "<a href=\"{}\" {}>{}</a>".format(link, kwstr, text)

def form(action, method, body, **kw):
    kwstr = attrs(**kw)
    return '<form action="{}" method="{}" {}>{}</form>'.format(action, method, kwstr, body)

def label(name, _for, **kw):
    kwstr = attrs(**kw)
    return '<label for="{}" {}>{}</label>'.format(_for, kwstr, name)

def textinput(name, default, **kw):
    kwstr = attrs(**kw)
    return '<input type="text" name="{}" default="{}" {}/>'.format(name, default, kwstr)

def submit(value, **kw):
    kwstr = attrs(**kw)
    assert '"' not in value
    return '<button type="submit" {}>{}</button>'.format(kwstr, value)

website = div(
            div(
                div(
                    div(
                        div(
                            h1("Jude C. Nelson",
                            _class="cover-heading", align="center") +
                            div(
                                div(
                                    div(
                                        p("Research Scientist at " + a("Stacks Open Internet Foundation", "https://stacks.org") + ".<br>Distributed Systems PhD, Princeton '18 (" + a("thesis", "ftp://ftp.cs.princeton.edu/techreports/2018/014.pdf") + ", " + a("CV", "cv.pdf") + ").",
                                        align="center", _class="lead"),
                                    _class="col-md-6 col-md-offset-3"),
                                _class="row"),
                            _class="container-fluid") +
                            img("me.jpg",
                            _class="img-circle", style="float-center", width="10%"),
                        _class="cover-heading", align="center"),
                    _class="inner-cover"),
                _class="container") +
                div(
                    div(
                        div(
                            h2("Background", align="center") +
                            "<br>" +
                            p("An academic computer scientist who escaped the lab.") +
                            p("<b>Professional Goals</b>:") +
                            ul(
                                li("Make users own their identites and data online.") +
                                li("Make surveillance capitalism unprofitable.") +
                                li("Make data silos a liability.")
                            ) +
                            p("<b>Training</b>:") +
                            ul(
                                li("PhD from Princeton in May 2018") +
                                li("MA from Princeton in October 2012") +
                                li("BS from University of Arizona in May 2010")
                            ) +
                            p("<b>Industry</b>:") +
                            ul(
                                li(a("Stacks Open Internet Foundation", "https://stacks.org") + " (2020-present)") +
                                li(a("Blockstack", "https://stacks.co") + " (2015-2020)") +
                                li("IBM -- DFSMShsm team (2008-2010)")
                            ),
                        _class="col-md-4") +
                        div(
                            h2("Selected Publications", align="center") +
                            "<br>" +
                            p("A few papers I helped write:") +
                            ul(
                                li("Ali, M., <b>Nelson, J.</b>, Shea, R., Freedman, M.  " + a("\"Blockstack: Design and Implementation of a Global Naming System with Blockchains.\"", "https://www.usenix.org/system/files/conference/atc16/atc16_paper-ali.pdf") + "  USENIX Annual Technical Conference 2016.  June 22-24, 2016.  Denver, CO, USA.") +
                                li("<b> Nelson, J.</b>, Ali, M., Shea, R., Freedman, M.  " + a("\"Extending Existing Blockchains with Virtualchain.\"", "https://www.zurich.ibm.com/dccl/papers/nelson_dccl.pdf") + "  Distributed Cryptocurrencies and Consensus Ledgers 2016.  July 25, 2016.  Chicago, IL, USA.") +
                                li("<b>Nelson, J.</b> and Peterson, L.  " + a("\"Syndicate: Virtual Cloud Storage through Provider Composition.\"", "https://pdfs.semanticscholar.org/4203/f4b5c6554f06ec719ee5b98ba86e4d33ee71.pdf") + "  ACM 1st Internation Workshop on Software-defined Ecosystems.  June 25, 2014.  Vancouver, British Columbia, Canada."),
                            ) +
                            p("A few patents I helped write:") +
                            ul(
                                li("<b>Nelson, J.,</b>, Blankstein, A., Salibra, L., Liao, K., Little., M.  " + a("\"Platform and associated method for authenticating the identity of a user in a decentralized system without need for a third-party identity service\"", "http://patft.uspto.gov/netacgi/nph-Parser?Sect1=PTO1&Sect2=HITOFF&d=PALL&p=1&u=%2Fnetahtml%2FPTO%2Fsrchnum.htm&r=1&f=G&l=50&s1=10,601,829.PN.&OS=PN/10,601,829&RS=PN/10,601,829")) +
                                li("<b>Nelson, J.,</b>"  + a("\"Systems and methods for forming application-specific blockchains\"", "http://patft.uspto.gov/netacgi/nph-Parser?Sect1=PTO1&Sect2=HITOFF&d=PALL&p=1&u=%2Fnetahtml%2FPTO%2Fsrchnum.htm&r=1&f=G&l=50&s1=10,698,728.PN.&OS=PN/10,698,728&RS=PN/10,698,728")) +
                                li("Blankstein, A., <b>Nelson, J.</b>" + a("\"System and method for smart contract publishing\"", "http://patft.uspto.gov/netacgi/nph-Parser?Sect1=PTO1&Sect2=HITOFF&d=PALL&p=1&u=%2Fnetahtml%2FPTO%2Fsrchnum.htm&r=1&f=G&l=50&s1=10,699,269.PN.&OS=PN/10,699,269&RS=PN/10,699,269")),
                            ),
                        _class="col-md-4") +
                        div(
                            h2("Open Source", align="center") +
                            "<br>" +
                            p("Some repositories I work on:") +
                            ul(
                                li(a("Stacks 2.0", "https://github.com/blockstack/stacks-blockchain") + ":  The reference implementation of the " + a("Stacks Blockchain", "https://stacks.co")) +
                                li(a("SIPs", "https://github.com/stacksgov/sips") + ": I am the Chair of the Technical Steering Committee of the Stacks Improvement Proposal process") +
                                li(a("Gaia", "https://github.com/blockstack/gaia") + ": A high-performance decentralized storage system used by Blockstack dapps.")
                            ) +
                            p("Some personal projects:") +
                            ul(
                                li(a("vdev", "https://github.com/jcnelson/vdev") + ":  A device maanger for UNIX-like systems.") +
                                li(a("runfs", "https://github.com/jcnelson/runfs") + ":  A self-cleaning RAM filesystem.") +
                                li(a("Syndicate", "https://github.com/syndicate-storage") + ": A scalable software-defined storage system for wide-area networks.")
                            ),
                        _class="col-md-4"),
                    _class="row"),
                _class="container"),
            _class="site-wrapper-inner"),
          _class="site-wrapper")


panel = '<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">\n'
panel += "<html lang=\"en\"><head><title>Jude C. Nelson</title>"
panel += "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">"

for s in CSS_PATHS:
    panel += '<link rel="stylesheet" href="{}">'.format(s)

for s in SCRIPTS:
    panel += '<script type="text/javascript" src="{}"></script>'.format(s)

panel += "</head><body>" + website + "</body></html>"

print panel
