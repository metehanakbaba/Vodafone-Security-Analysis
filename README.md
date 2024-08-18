# My Vodafone Uygulamasında SSL Pinning Bypass ve Network Trafiği İnceleme ile Zafiyet Keşfi

## 1. Giriş
Bu çalışmada, Vodafone’un iPhone uygulamasının 17.2.5 sürümünde SSL pinning korumasını aşarak network trafiğini izleyebildim ve bu sayede güvenlik açıklarını tespit edebildim. Bu süreç, bug bounty programlarına yönelik olarak hazırlanmış ve ilgili kişilere açıkların nasıl keşfedildiğini gösteren bir doküman niteliğindedir.

## 2. SSL Pinning Nedir?
SSL Pinning, bir uygulamanın yalnızca belirli sertifikalara sahip sunucularla iletişim kurmasına izin vererek, MITM (Man-in-the-Middle) saldırılarını önlemeye yardımcı olur. Bu koruma olmadan, saldırganlar araya girerek şifreli trafiği deşifre edebilir ve hassas bilgileri elde edebilir.

## 3. SSL Pinning Nasıl Aşıldı?
Bu güvenlik kontrolü, root edilmiş veya jailbreak yapılmış cihazlar üzerinde çeşitli araçlar kullanılarak aşılabilir. Bu çalışmada, iPhone cihazda SSL pinning’i devre dışı bırakmak için bir ara sertifika yerleştirildi. Bu sertifika, cihaz ile uygulama sunucusu arasındaki trafiği deşifre edebilmeyi sağladı.

## 4. Network Trafiği İnceleme
SSL pinning’i devre dışı bıraktıktan sonra, uygulamanın sunucuya gönderdiği ve sunucudan aldığı tüm HTTP(S) istekleri analiz edilebildi. Bu analiz, belirli bir API endpoint’inin nasıl çalıştığını, gönderilen verileri ve bu verilerin nasıl işlenip cevaplandığını görmemi sağladı.

## 5. Keşfedilen Zafiyetler
- **Authentication Bypass**: Giriş işlemlerini simüle ederek, uygulamaya sahte kimlik doğrulama bilgileri gönderildi ve bu sayede oturum açma işlemi gerçekleştirildi.
- **SMS Doğrulama Atlatma**: SMS doğrulama kodu, başarılı bir giriş yapmak için gerekli olan tek engel olarak belirlendi. Bu kodu elde etmek için kullanılan yöntemlerin yeterince güvenli olmadığı tespit edildi.
- **Promo Kampanyalarının Kötüye Kullanımı**: Uygulama içindeki promosyon kampanyaları (örneğin, 50GB internet kampanyası) sahte taleplerle suistimal edildi.

## 6. Önerilen Önlemler
- **Güçlü SSL Pinning**: Uygulamanın SSL pinning yöntemlerinin güçlendirilmesi ve sadece bilinen güvenilir sertifikalara izin verilmesi.
- **Çok Faktörlü Kimlik Doğrulama**: SMS doğrulamasının yanı sıra başka faktörler eklenerek kimlik doğrulama sürecinin daha güvenli hale getirilmesi.
- **İşlem Doğrulama Mekanizmaları**: Promosyon kampanyaları gibi işlemler için ek güvenlik kontrolleri getirilerek, bu işlemlerin kötüye kullanılmasının önüne geçilmesi.

## 7. Sonuç
Bu doküman, My Vodafone uygulamasının güvenlik açıklarını ve bu açıkların nasıl tespit edildiğini anlatmaktadır. Bug bounty programlarına bu zafiyetlerin raporlanması, hem uygulamanın güvenliğini artıracak hem de kullanıcılara daha güvenli bir deneyim sunulmasına katkı sağlayacaktır.

---

# SSL Pinning Bypass and Network Traffic Analysis in My Vodafone App: Vulnerability Discovery

## 1. Introduction
In this study, I was able to bypass the SSL pinning protection in version 17.2.5 of Vodafone's iPhone application, allowing me to monitor network traffic and identify security vulnerabilities. This process is documented as a guide for bug bounty programs, showing how these vulnerabilities were discovered.

## 2. What is SSL Pinning?
SSL Pinning helps prevent MITM (Man-in-the-Middle) attacks by allowing an application to communicate only with servers that have specific certificates. Without this protection, attackers can intercept encrypted traffic, potentially accessing sensitive information.

## 3. How SSL Pinning Was Bypassed
This security control can be bypassed on rooted or jailbroken devices using various tools. In this study, an intermediate certificate was installed on an iPhone to disable SSL pinning, enabling the decryption of traffic between the device and the application server.

## 4. Network Traffic Analysis
After bypassing SSL pinning, all HTTP(S) requests sent and received by the application could be analyzed. This analysis revealed how a specific API endpoint works, the data being sent, and how this data is processed and responded to.

## 5. Discovered Vulnerabilities
- **Authentication Bypass**: By simulating login processes, fake authentication credentials were sent to the application, successfully completing the login process.
- **SMS Verification Bypass**: The SMS verification code was identified as the only barrier to successful login. The methods used to obtain this code were found to be insufficiently secure.
- **Promo Campaign Abuse**: Promotional campaigns within the application (e.g., the 50GB internet campaign) were exploited using fake requests.

## 6. Recommended Measures
- **Strong SSL Pinning**: Strengthening the SSL pinning methods of the application to allow only trusted certificates.
- **Multi-Factor Authentication**: Enhancing the authentication process by adding additional factors alongside SMS verification.
- **Transaction Verification Mechanisms**: Implementing additional security checks for processes like promotional campaigns to prevent misuse.

## 7. Conclusion
This document details the security vulnerabilities of the My Vodafone application and how they were identified. Reporting these vulnerabilities to bug bounty programs will not only enhance the security of the application but also contribute to providing a safer experience for users.

---

## How to Install and Run

### Install the Package Locally

To install the package locally, run the following command:

```sh
pip install -e .
