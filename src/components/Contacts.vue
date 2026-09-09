<template>
  <section class="contacts">
    <header class="contacts__header">
      <h2 class="contacts__title">Контактна інформація</h2>
      <p class="contacts__subtitle">
        Відскануйте QR-код для швидкого збереження або переходу
      </p>
    </header>

    <div class="contacts__grid">
      <div
        v-for="item in contactItems"
        :key="item.type"
        :class="['contact-card', `contact-card--${item.type}`]"
      >
        <div class="contact-card__icon">
          <!-- Email SVG -->
          <svg v-if="item.type === 'email'" viewBox="0 0 24 24" width="32" height="32" fill="none" stroke="#00a53f" stroke-width="2">
            <path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z" />
            <polyline points="22,6 12,13 2,6" />
          </svg>
          <!-- Phone SVG -->
          <svg v-else-if="item.type === 'phone'" viewBox="0 0 24 24" width="32" height="32" fill="none" stroke="#3b82f6" stroke-width="2">
            <path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z" />
          </svg>
          <!-- Site SVG -->
          <svg v-else-if="item.type === 'site'" viewBox="0 0 24 24" width="32" height="32" fill="none" stroke="#f59e0b" stroke-width="2">
            <circle cx="12" cy="12" r="10" />
            <line x1="2" y1="12" x2="22" y2="12" />
            <path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z" />
          </svg>
        </div>
        <div class="contact-card__content">
          <span class="contact-card__label">{{ item.label }}</span>
          <div class="contact-card__value">{{ item.value }}</div>
        </div>
        <div class="contact-card__qr-box">
          <img
            :src="item.qr"
            :alt="item.label"
            class="contact-card__qr-img"
          />
          <span class="contact-card__qr-hint">{{ item.qrHint }}</span>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup lang="ts">
const base = import.meta.env.BASE_URL;

const contactItems = [
  {
    type: "email",
    label: "Електронна пошта",
    value: "oc_snau@ukr.net",
    qr: `${base}img/qr/email.jpg`,
    qrHint: "Сканувати Email",
  },
  {
    type: "phone",
    label: "Приймальна комісія / Телефон",
    value: "+38 (05446) 2-20-66",
    qr: `${base}img/qr/telephone.jpg`,
    qrHint: "Сканувати номер",
  },
  {
    type: "site",
    label: "Офіційний сайт",
    value: "ocsnau.net",
    qr: `${base}img/qr/ocsnau.jpg`,
    qrHint: "Перейти на сайт",
  },
];
</script>

<style scoped>
/* ==========================================================================
   Блок: contacts (Контактна інформація)
   Методологія: БЕМ
   ========================================================================== */

.contacts {
  width: 100%;
  min-height: 65vh;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  padding: 20px;
  font-family: system-ui, -apple-system, sans-serif;
  background-color: #ffffff;
}

.contacts__header {
  text-align: center;
  margin-bottom: 40px;
}

.contacts__title {
  font-size: 2.8rem;
  font-weight: 800;
  color: #166534;
  text-transform: uppercase;
  letter-spacing: 1px;
  margin: 0 0 10px 0;
}

.contacts__subtitle {
  font-size: 1.3rem;
  color: #64748b;
  margin: 0;
}

.contacts__grid {
  display: flex;
  flex-wrap: wrap;
  gap: 35px;
  justify-content: center;
  align-items: stretch;
  width: 100%;
  max-width: 1250px;
  margin: 0 auto;
}

/* ==========================================================================
   Блок: contact-card (Картка контакту)
   ========================================================================== */

.contact-card {
  width: 360px;
  background: #f8fafc;
  border: 1px solid #e2e8f0;
  border-radius: 24px;
  padding: 30px 20px;
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  box-shadow: 0 10px 25px rgba(0, 0, 0, 0.04);
  position: relative;
  overflow: hidden;
  transition: transform 0.25s ease, box-shadow 0.25s ease;
}

.contact-card::before {
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 6px;
}

.contact-card--email::before { background: #00a53f; }
.contact-card--phone::before { background: #3b82f6; }
.contact-card--site::before { background: #f59e0b; }

.contact-card:hover {
  transform: translateY(-8px);
  background: #ffffff;
  box-shadow: 0 20px 40px rgba(0, 0, 0, 0.08);
}

.contact-card__icon {
  font-size: 2.8rem;
  margin-bottom: 12px;
  background: #ffffff;
  width: 65px;
  height: 65px;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 50%;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.04);
}

.contact-card__content {
  margin-bottom: 20px;
  flex-grow: 1;
}

.contact-card__label {
  display: block;
  font-size: 1rem;
  font-weight: 700;
  color: #64748b;
  text-transform: uppercase;
  margin-bottom: 6px;
}

.contact-card__value {
  font-size: 1.5rem;
  font-weight: 800;
  color: #1e293b;
  word-break: break-all;
  line-height: 1.25;
}

.contact-card__qr-box {
  background: #ffffff;
  border: 2px solid #e2e8f0;
  padding: 12px;
  border-radius: 18px;
  display: flex;
  flex-direction: column;
  align-items: center;
  width: 160px;
}

.contact-card__qr-img {
  width: 130px;
  height: 130px;
  object-fit: contain;
  margin-bottom: 6px;
}

.contact-card__qr-hint {
  font-size: 0.8rem;
  font-weight: 700;
  color: #94a3b8;
  text-transform: uppercase;
}
</style>
