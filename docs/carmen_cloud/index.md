---
title: "คู่มือระบบ Carmen Cloud"
title_en: "Carmen Cloud System Guide"
lang: th-TH
module: carmen_cloud
submodule: overview
doc_type: overview
complexity: beginner
tags: [overview, introduction, getting_started]
country_specific: generic
target_audience: accountant
---

# Carmen Cloud Documentation

## บทนำ (Introduction)

**Carmen Cloud** คือระบบบัญชีและการจัดการธุรกิจแบบครบวงจรบนระบบคลาวด์ ออกแบบมาเพื่อสนับสนุนธุรกิจในภูมิภาคเอเชียตะวันออกเฉียงใต้ โดยเฉพาะประเทศไทยและฟิลิปปินส์ ระบบครอบคลุมการจัดการบัญชี การจัดการสินทรัพย์ และการจัดการสินค้าคงคลัง

**Carmen Cloud** is a comprehensive cloud-based ERP system designed for businesses in Southeast Asia, particularly Thailand and the Philippines. It covers accounting, asset management, and inventory management.

---

## ภาพรวมโมดูลหลัก (Main Modules Overview)

### 1. Account Payable (AP) - บัญชีเจ้าหนี้

จัดการหนี้สินที่บริษัทต้องชำระให้ซัพพลายเออร์

- [AP Invoice](./ap/AP-invoice.md) - การบันทึกใบแจ้งหนี้เจ้าหนี้
- [AP Payment](./ap/AP-payment.md) - การบันทึกการจ่ายเงิน
- [AP Vendor](./ap/AP-vendor.md) - การจัดการข้อมูลเจ้าหนี้
- [Input Tax Reconciliation](./ap/AP-input_tax_reconciliation.md) - การปรับสมดุลภาษีซื้อ
- [Withholding Tax Reconciliation](./ap/AP-wht_reconciliation.md) - การปรับสมดุลภาษีหัก ณ ที่จ่าย

### 2. Account Receivable (AR) - บัญชีลูกหนี้

จัดการหนี้สินที่ลูกค้าติดยอดชำระให้บริษัท

- [AR Invoice](./ar/AR-invoice.md) - การสร้างใบแจ้งหนี้ลูกหนี้
- [AR Receipt](./ar/AR-receipt.md) - การบันทึกใบเสร็จรับเงิน
- [AR Contract](./ar/AR-contract.md) - การจัดการสัญญา

### 3. General Ledger (GL) - บัญชีแยกประเภท

สมุดบัญชีรายวันและบัญชีแยกประเภทหลัก

- [Journal Voucher](./gl/c-journal_voucher.md) - การสร้างสมุดรายวัน
- [Posting from AP](./gl/c-posting_ap.md) - การดึงข้อมูล AP เข้า GL
- [Posting from AR](./gl/c-posting_ar.md) - การดึงข้อมูล AR เข้า GL

### 4. Fixed Asset - สินทรัพย์

จัดการทะเบียนสินทรัพย์และการคำนวณค่าเสื่อม

- [Asset Register](./asset/AS-asset_register.md) - การลงทะเบียนสินทรัพย์
- [Asset Disposal](./asset/AS-asset_disposal.md) - การตัดจำหน่ายสินทรัพย์

### 5. Configuration - การตั้งค่าระบบ

ตั้งค่าพื้นฐานสำหรับระบบ

- [Chart of Accounts](./configuration/CF-chart_of_account.md) - ผังบัญชี
- [Currency & Exchange Rate](./configuration/CF-currency_exrate.md) - สกุลเงินและอัตราแลกเปลี่ยน
- [Departments](./configuration/CF-department.md) - แผนก/หน่วยงาน
- [Users](./configuration/CF-users.md) - ผู้ใช้งานระบบ

---

## ขั้นตอนการทำงานระหว่างโมดูล (Cross-Module Workflows)

### Procure-to-Pay (การจัดซื้อจนจ่ายเงิน)

```
Purchase Order → Goods Receiving → AP Invoice → AP Payment → GL Posting
```

### Order-to-Cash (การขายจนรับเงิน)

```
AR Invoice → AR Receipt → GL Posting
```

### Asset Lifecycle (วงจรสินทรัพย์)

```
Asset Register → Monthly Depreciation → Disposal → GL Posting
```

---

## การเริ่มต้นใช้งาน (Getting Started)

1. **Configuration** - ตั้งค่าระบบพื้นฐาน (ผังบัญชี, แผนก, ผู้ใช้)
2. **Master Data** - สร้างข้อมูลหลัก (เจ้าหนี้, ลูกหนี้, รหัสบัญชี)
3. **Daily Operations** - บันทึกรายการประจำวัน (ใบแจ้งหนี้, การจ่ายเงิน)
4. **Posting** - ดึงข้อมูลเข้าสมุดบัญชีรายวัน
5. **Period Closing** - ปิดงวดบัญชีประจำเดือน

---

## เอกสารอ้างอิง (Reference)

- [Glossary](../glossary.md) - อภิธานศัพท์บัญชีไทย-อังกฤษ
- [AGENT.md](../AGENT.md) - คู่มือสำหรับ AI Agent
