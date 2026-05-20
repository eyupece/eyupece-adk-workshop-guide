# Google ADK Workshop Rehberi

Bu rehber, Google Agent Development Kit (ADK) ile bir müşteri hizmetleri agent'ı oluşturmayı ve değerlendirmeyi adım adım anlatır.

**Slide Linki:** https://docs.google.com/presentation/d/1C1YfGnp_8mIzDkQqepyuJ2uV5l1uaEFI9XrHiIc1hvI/edit?usp=sharing
**Yayın Linki:** https://www.youtube.com/watch?v=S_d-BtBcbpk  
**Starter Repo:** https://github.com/cuppibla/adk_eval_starter  
**ADK Dokümantasyonu:** https://adk.dev/

---

## Katılımcılar İçin Hızlı Akış

Bu workshopta sırasıyla şunları yapacağız:

1. Cloud Shell'i açacağız
2. Starter projeyi indireceğiz
3. Setup script'ini çalıştıracağız
4. ADK Web UI'ı başlatacağız
5. Agent'a test mesajı göndereceğiz
6. Evaluation çıktısını birlikte inceleyeceğiz

> **Not:** Evaluation ve Pytest bölümleri sunum akışına göre eğitmen yönlendirmesiyle kullanılacaktır.

---

## 1. Cloud Shell'i Açın

https://shell.cloud.google.com/ adresine gidin.

Hesabınızı kontrol edin:

```bash
gcloud auth list
```

---

## 2. Projeyi İndirin

```bash
git clone https://github.com/cuppibla/adk_eval_starter
```

> **"already exists" hatası alırsanız:**
> ```bash
> rm -rf ~/adk_eval_starter
> git clone https://github.com/cuppibla/adk_eval_starter
> ```

---

## 3. Setup

Proje klasörüne girip setup script'ini çalıştırın:

```bash
cd ~/adk_eval_starter
./init.sh
```

> Project ID sorarsa **Enter**'a basarak önerilen değeri kabul edebilirsiniz.

Google Cloud projesini terminale set edin:

```bash
gcloud config set project $(cat ~/project_id.txt) --quiet
```

Kontrol etmek için:

```bash
gcloud config get-value project
```

Gerekli servisleri aktif edin:

```bash
gcloud services enable \
  cloudresourcemanager.googleapis.com \
  servicenetworking.googleapis.com \
  run.googleapis.com \
  cloudbuild.googleapis.com \
  artifactregistry.googleapis.com \
  aiplatform.googleapis.com \
  compute.googleapis.com
```

Environment ayarlarını yükleyin:

```bash
. ~/adk_eval_starter/set_env.sh
```

Setup tamamlandı!

---

## 4. Demo — Agent'ı Çalıştırın

Proje klasöründe olduğunuzdan emin olun:

```bash
cd ~/adk_eval_starter
```

ADK Web UI'ı başlatın:

```bash
uv run adk web
```

Tarayıcıdan **Web Preview > Port 8000** ile arayüzü açın.

> **CORS hatası alırsanız** (Cloud Shell preview üzerinden mesaj gönderirken):
> ```bash
> uv run adk web --allow_origins 'regex:https://.*\.cloudshell\.dev'
> ```

### Test Mesajı

Agent chat ekranına şu mesajı yazın:

**İngilizce:**
```
Hi, I'm customer CUST001. Can you check my orders? I need a refund for order ORD-102. It arrived damaged.
```

**Türkçe:**
```
Merhaba, ben CUST001 numaralı müşteriyim. Siparişlerimi kontrol edebilir misiniz? ORD-102 numaralı sipariş için iadeye ihtiyacım var. Sipariş hasarlı geldi.
```

---

## 5. Opsiyonel: Evaluation Komutları

> Bu bölüm, sunum sırasında eğitmen yönlendirmesiyle kullanılacaktır.  
> İlk kurulum ve demo için bu bölümü hemen çalıştırmanız gerekmez.

### Eval Dosyalarını İndirin

Aşağıdaki komutlar gerekli evaluation dosyalarını proje içinde oluşturacaktır.

```bash
cd ~/adk_eval_starter

curl -L -o customer_service_agent/test_config.json \
  https://raw.githubusercontent.com/eyupece/adk-workshop-guide/main/files/test_config.json

curl -L -o customer_service_agent/eval.test.json \
  https://raw.githubusercontent.com/eyupece/adk-workshop-guide/main/files/eval.test.json

curl -L -o customer_service_agent/test_agent_eval.py \
  https://raw.githubusercontent.com/eyupece/adk-workshop-guide/main/files/test_agent_eval.py
```

### CLI ile Eval Çalıştırma

```bash
uv run adk eval customer_service_agent \
  customer_service_agent/eval.test.json \
  --config_file_path=customer_service_agent/test_config.json \
  --print_detailed_results
```

### Pytest ile Eval Çalıştırma

```bash
uv pip install pytest
uv run pytest customer_service_agent/test_agent_eval.py -v
```

---

## Sorun Giderme

### Sürüm Kontrolü

```bash
uv run adk --version
```

Eğer sürüm sorunu varsa:

```bash
cd ~/adk_eval_starter
rm -f uv.lock
rm -rf .venv
uv sync
uv run adk --version
```

### Web UI Açılmıyor

Cloud Shell'de **Web Preview** butonuna tıklayıp **Port 8000**'i seçtiğinizden emin olun.

### Eval Dosyası Bulunamıyor

Dosyaların doğru yerde olduğunu kontrol edin:

```bash
ls -la customer_service_agent/*.json
```

---

## Faydalı Linkler

- [Google ADK Dokümantasyonu](https://adk.dev/)
- [Cloud Shell](https://shell.cloud.google.com/)
- [Starter Repo](https://github.com/cuppibla/adk_eval_starter)
- [Slide Linki]([https://github.com/cuppibla/adk_eval_starter](https://docs.google.com/presentation/d/1C1YfGnp_8mIzDkQqepyuJ2uV5l1uaEFI9XrHiIc1hvI/edit?usp=sharing))
- [Yayın Linki](https://www.youtube.com/watch?v=S_d-BtBcbpk)
