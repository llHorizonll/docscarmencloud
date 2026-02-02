---
title: "คู่มือโมดูล General Ledger"
title_en: "General Ledger Module Guide"
lang: th-TH
module: carmen_cloud
submodule: gl
doc_type: overview
complexity: beginner
tags: [gl, overview, general_ledger, บัญชีแยกประเภท]
country_specific: generic
target_audience: accountant
---

# General Ledger Module Overview

## ภาพรวม (Overview)

**General Ledger (GL)** หรือ **บัญชีแยกประเภท** เป็นโมดูลหลักสำหรับบันทึกสมุดบัญชีรายวัน รวบรวมข้อมูลจากโมดูลอื่น ๆ และจัดทำรายงานทางการเงิน

**General Ledger (GL)** is the main module for recording journal vouchers, consolidating data from other modules, and generating financial reports.

---

## หน้าที่หลัก (Key Functions)

| หน้าที่ | Function | คำอธิบาย |
|---------|----------|-----------|
| สมุดบัญชีรายวัน | Journal Voucher | บันทึกรายการบัญชีแบบ Manual |
| ดึงข้อมูลจาก AP | Posting from AP | โอนย้ายข้อมูล AP เข้าสมุดบัญชีรายวัน |
| ดึงข้อมูลจาก AR | Posting from AR | โอนย้ายข้อมูล AR เข้าสมุดบัญชีรายวัน |
| ดึงข้อมูลจากสินทรัพย์ | Posting from Asset | โอนย้ายข้อมูลค่าเสื่อมเข้าสมุดบัญชีรายวัน |
| ดึงข้อมูลจากสินค้าคงคลัง | Posting from Inventory | โอนย้ายข้อมูลสินค้าคงคลังเข้าสมุดบัญชีรายวัน |
| งบประมาณ | Budget | จัดการงบประมาณ |
| ใบสำคัญอื่น ๆ | Other Vouchers | Allocation, Recurring, Amortization |

---

## โครงสร้างบัญชี (Chart of Accounts Structure)

### หมวดบัญชี (Account Nature)

| หมวด | Nature | คำอธิบาย | Balance |
|------|--------|-----------|---------|
| หมวด 1 | Assets | สินทรัพย์ | Debit |
| หมวด 2 | Liabilities | หนี้สิน | Credit |
| หมวด 3 | Equity | ทุน | Credit |
| หมวด 4 | Revenue | รายได้ | Credit |
| หมวด 5 | Expenses | ค่าใช้จ่าย | Debit |

### ประเภทรหัสบัญชี (Account Type)

| Type | คำอธิบาย |
|------|-----------|
| **Header** | หมวดบัญชีคุม (ไม่ถูกนำไปคำนวณ) |
| **Balance Sheet** | รหัสบัญชีในงบดุล |
| **Income Statement** | รหัสบัญชีในงบกำไรขาดทุน |
| **Statistic** | รหัสบัญชีสถิติ |

---

## ขั้นตอนการทำงาน (Workflow)

### 1. การบันทึกสมุดบัญชีรายวันแบบ Manual

```
GL Module → Journal Voucher → Add → Enter Data → Save
```

### 2. การดึงข้อมูลจากโมดูลอื่น

```
Sub-ledger (AP/AR/Asset) → Posting Function → GL (Journal Voucher)
```

### 3. การใช้งาน Template

```
Template → Create from JV → Apply Template → Modify → Save
```

---

## ประเภท Journal Voucher

### 1. Journal Voucher (JV)

ใบสำคัญบันทึกบัญชีทั่วไป ใช้สำหรับบันทึกรายการที่ไม่ได้จากโมดูลอื่น

### 2. Allocation Voucher

ใบสำคัญจัดสรรค่าใช้จ่าย ใช้สำหรับกระจายค่าใช้จ่ายร่วมไปยังแผนกต่าง ๆ

### 3. Recurring Voucher

ใบสำคัญประจำงวด ใช้สำหรับรายการที่เกิดซ้ำทุกเดือน

### 4. Amortization Voucher

ใบสำคัญคำนวณค่าเสื่อมและการกระจายค่าใช้จ่ายล่วงหน้า

---

## การทำงานกับ Journal Voucher

### การสร้าง JV แบบ Manual

1. เข้า General Ledger Module
2. เลือก Journal Voucher
3. กดปุ่ม Add
4. ระบุข้อมูล Header (Prefix, Date, Description)
5. กดปุ่ม + เพื่อเพิ่มรายการ
6. ระบุรายการบัญชี (Department, Account, Amount)
7. บันทึกเมื่อ Dr. = Cr.

### การใช้งาน Copy Function

| ประเภท | คำอธิบาย |
|--------|-----------|
| Copy to new JV | คัดลอกไปสร้าง JV ใบใหม่ |
| Copy and reverse | คัดลอกและกลับขาบัญชี |
| Copy with zero amount | คัดลอกโดยไม่มียอดเงิน |
| Copy to Template | คัดลอกไปเป็น Template |

### การใช้งาน Template

```
Create JV → Copy to Template → Use Template → Select Template → Modify → Save
```

---

## เอกสารที่เกี่ยวข้อง (Related Documents)

- [Journal Voucher](./c-journal_voucher.md) - การสร้างสมุดบัญชีรายวัน
- [Allocation Voucher](./c-allocation_voucher.md) - ใบสำคัญจัดสรร
- [Recurring Voucher](./c-recurring_voucher.md) - ใบสำคัญประจำงวด
- [Amortization Voucher](./c-amortization_voucher.md) - ใบสำคัญคำนวณค่าเสื่อม
- [Template Voucher](./c-template_voucher.md) - การใช้งาน Template
- [Financial Report](./c-FinancialGL.md) - รายงานทางการเงิน
- [Posting from AP](./c-posting_ap.md) - การดึงข้อมูล AP เข้า GL
- [Posting from AR](./c-posting_ar.md) - การดึงข้อมูล AR เข้า GL
- [Posting from Asset](./c-posting_asset.md) - การดึงข้อมูลสินทรัพย์เข้า GL
- [Posting from Inventory](./c-posting_inventory.md) - การดึงข้อมูลสินค้าคงคลังเข้า GL

---

## คำถามที่พบบ่อย (FAQ)

### Q: Debit และ Credit ต้องเท่ากันเสมอหรือไม่?

**A:** ใช่ การบันทึกบัญชีแต่ละครั้งต้องมี Debit และ Credit เท่ากันเสมอ (Double Entry)

### Q: สามารถแก้ไข JV ได้หรือไม่?

**A:** แก้ไขได้ แต่หากถูกโพสต์หรือ Period ถูกปิดไปแล้วจะแก้ไขไม่ได้

### Q: ข้อมูลจาก AP และ AR จะไปอยู่ที่ไหนใน GL?

**A:** ข้อมูลจะถูกสร้างเป็น Journal Voucher โดยอัตโนมัติเมื่อทำการ Posting

---

## เงื่อนไขผิดพลาดทั่วไป (Common Issues)

| ปัญหา | สาเหตุ | วิธีแก้ไข |
|--------|---------|-------------|
| Dr ≠ Cr | รายการไม่สมดุล | ตรวจสอบยอดเงินทุกรายการ |
| บันทึกไม่สำเร็จ | Period ปิดแล้ว | ตรวจสอบสถานะ Period |
| Account Code ผิด | รหัสบัญชีไม่ถูกต้อง | ตรวจสอบ Chart of Accounts |
| ไม่สามารถลบ | ถูกโพสต์แล้ว | ต้องทำ Reversal แทนการลบ |

---

## ดูเพิ่มเติม (See Also)

- [Account Payable Overview](../ap/overview.md)
- [Account Receivable Overview](../ar/overview.md)
- [Asset Overview](../asset/overview.md)
- [Chart of Accounts Configuration](../configuration/CF-chart_of_account.md)
