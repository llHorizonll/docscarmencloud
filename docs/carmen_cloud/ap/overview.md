---
title: "คู่มือโมดูล Account Payable"
title_en: "Account Payable Module Guide"
lang: th-TH
module: carmen_cloud
submodule: ap
doc_type: overview
complexity: beginner
tags: [ap, overview, account_payable, เจ้าหนี้]
country_specific: generic
target_audience: accountant
---

# Account Payable Module Overview

## ภาพรวม (Overview)

**Account Payable (AP)** หรือ **บัญชีเจ้าหนี้** เป็นโมดูลสำหรับบันทึกและจัดการหนี้สินที่บริษัทต้องชำระให้กับซัพพลายเออร์หรือผู้ขายสินค้าบริการ

**Account Payable (AP)** is the module for recording and managing debts that the company must pay to suppliers or service providers.

---

## หน้าที่หลัก (Key Functions)

| หน้าที่ | Function | คำอธิบาย |
|---------|----------|-----------|
| บันทึกใบแจ้งหนี้ | Invoice | บันทึกใบแจ้งหนี้จากเจ้าหนี้ |
| บันทึกการจ่ายเงิน | Payment | บันทึกการชำระหนี้และออกเช็ค |
| จัดการข้อมูลเจ้าหนี้ | Vendor Profile | สร้างและแก้ไขข้อมูลเจ้าหนี้ |
| ปรับสมดุลภาษีซื้อ | Input Tax Reconciliation | ตรวจสอบและปรับภาษีซื้อ |
| ปรับสมดุลภาษีหัก ณ ที่จ่าย | WHT Reconciliation | ตรวจสอบและปรับภาษีหัก ณ ที่จ่าย |
| บันทึกมัดจำ | Deposit | บันทึกการรับและคืนมัดจำ |
| โอนย้ายข้อมูลภาษี | RDPrep | โอนข้อมูลไปโปรแกรม RDPrep |
| ปิดงวดบัญชี | Close Period | ปิดงวดบัญชี AP |

---

## ขั้นตอนการทำงาน (Workflow)

### 1. การตั้งค่าเบื้องต้น (Initial Setup)

```
Configuration → Chart of Accounts → Vendor Profile
```

### 2. การบันทึกรายการประจำวัน (Daily Transactions)

```
Receive Invoice → Record AP Invoice → Record Payment (when paid)
```

### 3. การจัดการภาษี (Tax Management)

```
Invoice with Tax → Tax Reconciliation → RDPrep → Tax Filing
```

### 4. การส่งข้อมูลเข้า GL (Posting to GL)

```
AP Module → Posting from AP → General Ledger (Journal Voucher)
```

---

## สถานะภาษีในใบแจ้งหนี้ (Tax Status)

| สถานะ | คำอธิบาย | ผลกระทบต่อบัญชี |
|--------|-----------|------------------|
| **Confirm** | ได้รับใบกำกับภาษีแล้ว | บันทึก Dr. ภาษีซื้อ |
| **Pending** | ยังไม่ได้รับใบกำกับภาษี | บันทึก Dr. ภาษีซื้อตั้งพักไว้ |
| **Unclaim** | ใบกำกับภาษีที่ไม่สามารถขอคืนได้ | ไม่บันทึกภาษีซื้อ |
| **None** | ไม่มีภาษี | ไม่บันทึกภาษี |

---

## เอกสารที่เกี่ยวข้อง (Related Documents)

- [AP Invoice](./AP-invoice.md) - วิธีบันทึกใบแจ้งหนี้เจ้าหนี้
- [AP Payment](./AP-payment.md) - วิธีบันทึกการจ่ายเงิน
- [AP Vendor](./AP-vendor.md) - วิธีจัดการข้อมูลเจ้าหนี้
- [Input Tax Reconciliation (Thailand)](./AP-input_tax_reconciliation.md)
- [Input Tax Reconciliation (Philippines)](./AP-input_tax_reconciliationPhilippines.md)
- [WHT Reconciliation (Thailand)](./AP-wht_reconciliation.md)
- [WHT Reconciliation (Philippines)](./AP-wht_reconciliationPhilippines.md)
- [RDPrep PND.3](./AP-RDPrep_3.md) - โอนย้ายข้อมูล ภ.ง.ด.3
- [RDPrep PND.53](./AP-RDPrep_53.md) - โอนย้ายข้อมูล ภ.ง.ด.53
- [Posting from AP to GL](../gl/c-posting_ap.md)

---

## คำถามที่พบบ่อย (FAQ)

### Q: การบันทึกใบแจ้งหนี้ต้องใช้ข้อมูลอะไรบ้าง?

**A:** ข้อมูลที่จำเป็น ได้แก่:
- เลขที่ใบแจ้งหนี้ (Invoice No.)
- รหัสเจ้าหนี้ (Vendor)
- วันที่ใบแจ้งหนี้ (Invoice Date)
- สกุลเงินและอัตราแลกเปลี่ยน (Currency & Rate)
- รายละเอียดสินค้า/บริการ (Invoice Detail)

### Q: Tax Status คืออะไร? ควรเลือกอะไร?

**A:** Tax Status ใช้ระบุสถานะของใบกำกับภาษี:
- **Confirm** - เมื่อได้รับใบกำกับภาษีแล้ว
- **Pending** - เมื่อยังไม่ได้รับใบกำกับภาษี
- **Unclaim** - ใบกำกับภาษีที่ไม่สามารถนำไปลดหัดได้
- **None** - รายการที่ไม่มีภาษี

### Q: วิธีโพสต์ข้อมูล AP เข้า GL ทำอย่างไร?

**A:** ดูรายละเอียดได้ที่ [Posting from AP to GL](../gl/c-posting_ap.md)

---

## เงื่อนไขผิดพลาดทั่วไป (Common Issues)

| ปัญหา | สาเหตุ | วิธีแก้ไข |
|--------|---------|-------------|
| บันทึกไม่สำเร็จ | ข้อมูลไม่ครบถ้วน | ตรวจสอบฟิลด์ที่มีเครื่องหมาย * |
| ยอด Debit ≠ Credit | รายการบัญชีไม่สมดุล | ตรวจสอบรหัสบัญชีใน Invoice Detail |
| โพสต์ไม่ได้ | Period ถูกปิดไปแล้ว | ตรวจสอบสถานะ Period |
| ภาษีไม่ถูกต้อง | Tax Profile ผิด | ตรวจสอบการตั้งค่า Tax Profile |

---

## ดูเพิ่มเติม (See Also)

- [General Ledger Overview](../gl/overview.md)
- [Account Receivable Overview](../ar/overview.md)
- [Configuration Guide](../configuration/CF-chart_of_account.md)
