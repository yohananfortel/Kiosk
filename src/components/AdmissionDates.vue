<template>
  <div class="admission-dates">
    <h2 class="admission-dates__title">Терміни вступної кампанії</h2>

    <table class="admission-dates__table">
      <thead>
        <tr class="admission-dates__tr">
          <th class="admission-dates__th">Етап</th>
          <th class="admission-dates__th">На основі 9 класів (БСО)</th>
          <th class="admission-dates__th">
            На основі 11 класів (ПЗСО)<br />
            <span class="admission-dates__th-sub"
              >або диплома кваліфікованого робітника / раніше здобутої освіти</span
            >
          </th>
        </tr>
      </thead>
      <tbody>
        <tr class="admission-dates__tr">
          <td class="admission-dates__td">Реєстрація електронних кабінетів</td>
          <td class="admission-dates__td"><strong>25 червня – 15 жовтня</strong></td>
          <td class="admission-dates__td"><strong>1 липня – 15 жовтня</strong></td>
        </tr>
        <tr class="admission-dates__tr">
          <td class="admission-dates__td">Подання заяв на бюджет</td>
          <td class="admission-dates__td">
            <strong>1 липня – 20 липня</strong> (до 18:00)<br />
            <span class="admission-dates__td-sub"
              >(додатковий набір за умови зарахування не пізніше за 15 жовтня)</span
            >
          </td>
          <td rowspan="2" class="admission-dates__td">
            <strong>Бюджет:</strong> 1 липня – 20 липня<br /><br />
            <strong>Контракт:</strong><br />
            • 6 липня – 2 серпня (основа НМТ)<br />
            • 6 липня – 27 липня (співбесіда/творчий конкурс)
          </td>
        </tr>
        <tr class="admission-dates__tr">
          <td class="admission-dates__td">Подання заяв на контракт</td>
          <td class="admission-dates__td">-</td>
        </tr>
        <tr class="admission-dates__tr">
          <td class="admission-dates__td">Проведення співбесід, творчих конкурсів</td>
          <td class="admission-dates__td"><strong>21 липня – 28 липня</strong></td>
          <td class="admission-dates__td"><strong>27 липня – 7 серпня</strong></td>
        </tr>
        <tr class="admission-dates__tr">
          <td class="admission-dates__td">Оприлюднення рейтингових списків</td>
          <td class="admission-dates__td">
            <strong>29 липня</strong> (з 14:00) – <strong>31 липня</strong> (до 12:00)
          </td>
          <td class="admission-dates__td">
            <strong>8 серпня</strong> (з 12:00) – <strong>17 серпня</strong> (до 12:00)
          </td>
        </tr>
        <tr class="admission-dates__tr">
          <td class="admission-dates__td">Підтвердження вибору місця (бюджет)</td>
          <td class="admission-dates__td"><strong>4 серпня</strong> (до 18:00)</td>
          <td class="admission-dates__td"><strong>18 серпня</strong> (до 18:00)</td>
        </tr>
        <tr class="admission-dates__tr">
          <td class="admission-dates__td">Зарахування на бюджет</td>
          <td class="admission-dates__td"><strong>7 серпня</strong> (до 18:00)</td>
          <td class="admission-dates__td"><strong>19 серпня</strong> (до 18:00)</td>
        </tr>
        <tr class="admission-dates__tr">
          <td class="admission-dates__td">Зарахування на контракт</td>
          <td class="admission-dates__td">
            не пізніше за <strong>11 серпня</strong><br />
            <span class="admission-dates__td-sub">(додатковий набір – до 15 жовтня)</span>
          </td>
          <td class="admission-dates__td"><strong>30 серпня</strong> (до 18:00)</td>
        </tr>
        <tr class="admission-dates__tr">
          <td class="admission-dates__td">Переведення на вакантні бюджетні місця</td>
          <td class="admission-dates__td">не пізніше ніж <strong>17 серпня</strong></td>
          <td class="admission-dates__td">не пізніше ніж <strong>30 серпня</strong></td>
        </tr>
        <tr class="admission-dates__tr">
          <td class="admission-dates__td">Додатковий набір на контракт</td>
          <td class="admission-dates__td">не пізніше за <strong>15 жовтня</strong></td>
          <td class="admission-dates__td">не пізніше за <strong>15 жовтня</strong></td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<style scoped>
/* ==========================================================================
   Блок: admission-dates (Терміни вступної кампанії)
   Методологія: БЕМ
   ========================================================================== */

.admission-dates {
  width: 100%;
  font-family: system-ui, -apple-system, sans-serif;
}

.admission-dates__title {
  font-size: 2.5rem;
  font-weight: 800;
  color: #166534;
  margin-bottom: 25px;
  text-transform: uppercase;
  text-align: center;
}

.admission-dates__table {
  width: 100%;
  border-collapse: collapse;
  font-size: 1.25rem;
  text-align: left;
  border-radius: 16px;
  overflow: hidden;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.04);
}

.admission-dates__th {
  background-color: #166534;
  color: #ffffff;
  padding: 18px 20px;
  font-size: 1.35rem;
  font-weight: 800;
  border: 1px solid #14532d;
}

.admission-dates__th-sub {
  font-size: 0.95rem;
  font-weight: 500;
  color: #bbf7d0;
  display: block;
  margin-top: 4px;
}

.admission-dates__td {
  padding: 14px 20px;
  border: 1px solid #e2e8f0;
  color: #1e293b;
  vertical-align: top;
  line-height: 1.45;
}

.admission-dates__td-sub {
  font-size: 0.95rem;
  color: #64748b;
  display: block;
  margin-top: 3px;
}

.admission-dates__tr:nth-child(even) {
  background-color: #f8fafc;
}
</style>
