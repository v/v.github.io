---
layout: post
title: "Easy HTTPS Setup with StartSSL"
date: 2014-07-10 05:33"
published: true
---

If you're like me, you've written loads of web apps, but you rarely set up SSL on them. SSL is a must for any production-grade web application, especially if you're authenticating users or taking personal information from them. Otherwise all the contents of your HTTP requests are being sent in plaintext - user login info / passwords, cookies etc.

Usually, SSL certificates can cost lots of money ([Verisign charges over $100 / month](http://www.symantec.com/page.jsp?id=compare-ssl-certificates)), and be annoying to setup. After paying for domains and hosting, this is the last thing you want to shell out money for. Thus, [StartSSL Free](https://www.startssl.com/) is a very appealing product because it gives you a free SSL certificate valid for 1 year, that's accepted in all major browsers. I'm using it to serve [flipdclass.com](https://flipdclass.com) over SSL.

### Getting your Cerficates from StartSSL

- Start by [Signing up for an Account at StartSSL](https://www.startssl.com/?app=11&action=regform).
- They'll send you a verification code and install a client certificate into your browser.
- [Backup this certificate](https://www.startssl.com/?app=25#4) to cloud storage and [Sign in to StartSSL](https://auth.startssl.com/).
- Now, you'll want to validate your domain. Go to the [StartSSL Free Product Page](https://www.startssl.com/?app=12) >  Validations Wizard > Domain Name Validation. Type in your domain name (vverma.net for example).
- StartSSL will give you a list of email addresses for verifying your domain. You can usually access one of these emails through your domain registrar if you aren't already [set up to receive emails at your domain](http://www.labnol.org/internet/setup-outlook-on-custom-domain/24699/).
- Verify your domain (sometimes it takes a few minutes), and click on Cerficates Wizard to start creating your very first cert.
- Pick Web Server SSL/TLS Certificate > Enter a Password. Note the password that you enter - you will need it later to encrypt your private key.
- This will give you a private key in a text box. Copy this into a text editor and save the file as `domain_key.enc`.
- Click Continue > Continue > Add a Subdomain to your key. If you're making this for the top level domain (http://vverma.net), I would recommend adding `www` as the sub domain to the certificate. You'll need to create a certificate for each subdomain that you want to access over HTTPS, unless you get a wildcard SSL cert (not available through StartSSL Free). 
- On the next page, you'll see a certificate in a text box. Copy this into a text editor and save the file as `domain.crt`. I would also recommend saving the [intermediate](https://www.startssl.com/certs/sub.class1.server.ca.pem) and [root](https://www.startssl.com/certs/ca.pem) CA certs, because you'll need them for your webserver setup.

### Setting up your Web Server

I'll walk you through setting up nginx or apache for SSL.

- At this point you'll want to copy all the certificate files onto your server (`domain_key.enc, domain.crt, ca.pem, sub.class1.server.ca.pem` ), probably via scp.
- I'd recommend moving all certificate files to a directory like `/etc/nginx/ssl/`
- Now, you'll want to unencrypt your private key `domain_key.enc`, so that it can be read by your web server. Without this, your webserver will prompt you for a password everytime it is restarted.

```bash 
$ openssl rsa -in domain_key.enc -out domain.key 
$ chmod 400 domain.key # only root should be able to read this.
```

- Next, you'll want to configure your webserver to respond to HTTPS requests with the certificate.

#### Apache Virtual Host
```
<VirtualHost _default_:443>
    ServerName domain.com

    SSLEngine On

    SSLCertificateFile /path/to/certs/domain.crt
    SSLCertificateKeyFile /path/to/certs/domain.key
    SSLCertificateChainFile /path/to/certs/sub.class1.server.ca.pem

    ...
</VirtualHost>
```

#### Nginx Virtual Host

Nginx does not have a [directive for SSL Certificate Chains](http://nginx.org/en/docs/http/configuring_https_servers.html), so you will to concatenate your certificate to the intermediate and root CA certs.

```bash
$ cat domain.crt sub.class1.server.ca.pem ca.pem > domain.chained.crt
```

Then you can configure your virtual host as follows.

```
server {
    listen 443 default_server ssl;
    ssl_certificate /path/to/certs/domain.chained.crt;
    ssl_certificate_key /path/to/certs/domain.key;
    ...
}
```

Now, you can reload your webserver, and if you did everything correctly, you should get a successful HTTPS connection to your web app. Make sure that you test your site on a few different browsers, because not all browsers will behave the same way with SSL certificates.

You should also consider configuring your webserver to redirect all traffic to HTTPS, in order to prevent users from leaking their sensitive data by mistake.
