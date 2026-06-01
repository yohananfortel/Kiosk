<template>
  <div class="dates-container">
    <h2 class="modal-main-title">Терміни вступної кампанії</h2>

    <table class="dates-table">
      <thead>
        <tr>
          <th>Етап</th>
          <th>На основі 9 класів (БСО)</th>
          <th>
            На основі 11 класів (ПЗСО)<br /><span class="th-sub"
              >або диплома кваліфікованого робітника / раніше здобутої
              освіти</span
            >
          </th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>Реєстрація електронних кабінетів</td>
          <td><strong>25 червня – 15 жовтня</strong></td>
          <td><strong>1 липня – 15 жовтня</strong></td>
        </tr>
        <tr>
          <td>Подання заяв на бюджет</td>
          <td>
            <strong>1 липня – 20 липня</strong> (до 18:00)<br /><span
              class="td-sub"
              >(додатковий набір за умови зарахування не пізніше за 15
              жовтня)</span
            >
          </td>
          <td rowspan="2">
            <strong>Бюджет:</strong> 1 липня – 20 липня<br /><br />
            <strong>Контракт:</strong><br />
            • 6 липня – 2 серпня (основа НМТ)<br />
            • 6 липня – 27 липня (співбесіда/творчий конкурс)
          </td>
        </tr>
        <tr>
          <td>Подання заяв на контракт</td>
          <td>-</td>
        </tr>
        <tr>
          <td>Проведення співбесід, творчих конкурсів</td>
          <td><strong>21 липня – 28 липня</strong></td>
          <td><strong>27 липня – 7 серпня</strong></td>
        </tr>
        <tr>
          <td>Оприлюднення рейтингових списків</td>
          <td>
            <strong>29 липня</strong> (з 14:00) – <strong>31 липня</strong> (до
            12:00)
          </td>
          <td>
            <strong>8 серпня</strong> (з 12:00) – <strong>17 серпня</strong> (до
            12:00)
          </td>
        </tr>
        <tr>
          <td>Підтвердження вибору місця (бюджет)</td>
          <td><strong>4 серпня</strong> (до 18:00)</td>
          <td><strong>18 серпня</strong> (до 18:00)</td>
        </tr>
        <tr>
          <td>Зарахування на бюджет</td>
          <td><strong>7 серпня</strong> (до 18:00)</td>
          <td><strong>19 серпня</strong> (до 18:00)</td>
        </tr>
        <tr>
          <td>Зарахування на контракт</td>
          <td>
            не пізніше за <strong>11 серпня</strong><br /><span class="td-sub"
              >(додатковий набір – до 15 жовтня)</span
            >
          </td>
          <td><strong>30 серпня</strong> (до 18:00)</td>
        </tr>
        <tr>
          <td>Переведення на вакантні бюджетні місця</td>
          <td>не пізніше ніж <strong>17 серпня</strong></td>
          <td>не пізніше ніж <strong>30 серпня</strong></td>
        </tr>
        <tr>
          <td>Додатковий набір на контракт</td>
          <td>не пізніше за <strong>15 жовтня</strong></td>
          <td>не пізніше за <strong>15 жовтня</strong></td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<style scoped>
.modal-main-title {
  font-size: 2.5rem;
  color: #064e3b;
  margin-bottom: 2rem;
  text-transform: uppercase;
}

.dates-container {
  width: 100%;
}

.dates-table {
  width: 100%;
  border-collapse: collapse;
  font-family: "Roboto", sans-serif;
  font-size: 1.3rem;
  text-align: left;
}

.dates-table th {
  background-color: #166534;
  color: white;
  padding: 20px;
  font-size: 1.4rem;
  border: 2px solid #14532d;
}

.th-sub {
  font-size: 1rem;
  font-weight: normal;
  color: #bbf7d0;
}

.td-sub {
  font-size: 1rem;
  color: #64748b;
}

.dates-table td {
  padding: 15px 20px;
  border: 2px solid #e2e8f0;
  color: #1e293b;
  vertical-align: top;
  line-height: 1.4;
}

.dates-table tr:nth-child(even) {
  background-color: #f8fafc;
}
</style>
