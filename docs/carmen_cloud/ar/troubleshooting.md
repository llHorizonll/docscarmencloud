---
title: "AR Module Troubleshooting"
title_en: "Account Receivable Troubleshooting Guide"
lang: th-TH
module: carmen_cloud
submodule: ar
doc_type: troubleshooting
complexity: intermediate
tags: [ar, troubleshooting, error, account_receivable]
country_specific: generic
target_audience: accountant
---

# Account Receivable - แก้ปัญหา (Troubleshooting Guide)

## ปัญหาที่พบบ่อย (Common Issues)

---

## 1. บันทึก AR Invoice ไม่สำเร็จ

### Error Messages:
- "Cannot save invoice"
- "Customer not found"
- "Account code is required"
- "Total Dr ≠ Cr"
- "Invoice No already exists"

### Solutions:

#### 1.1 ตรวจสอบข้อมูลบังคับต้องกรอก
```
✓ Invoice No (เลขที่ใบแจ้งหนี้)
✓ A/R No (รหัสลูกค้า)
✓ Currency (สกุลเงิน)
✓ Rate (อัตราแลกเปลี่ยน)
✓ Invoice Date (วันที่ใบแจ้งหนี้)
✓ Due Date (วันที่ครบกำหนดชำระ)
✓ Invoice Detail (รายการสินค้า/บริการ อย่างน้อย 1 รายการ)
```

#### 1.2 ตรวจสอบ Tax Status
```
None → ไม่มีภาษี (ใบวางบิล)
Output Vat → มีภาษี (สำหรับขายสินค้าเท่านั้น)

หมายเหตุ: สำหรับบริการ ต้องสร้างใบกำกับภาษีเมื่อรับเงิน (Receipt) เท่านั้น
```

#### 1.3 ตรวจสอบ Account Code
```
Dr Acc Code → รหัสบัญชีลูกหนี้การค้า / รายได้
Cr Acc Code → รหัสบัญชีรายได้ / ภาษีขาย
```

---

## 2. รับเงิน (Receipt) ไม่ได้ / ตัดจ่าย Invoice ไม่ได้

### Error Messages:
- "Cannot select invoice for settlement"
- "Payment amount exceeds balance"
- "Cannot post receipt"

### Solutions:

#### 2.1 ตรวจสอบวิธีเลือก Invoice สำหรับตัดจ่าย
```
1. กดปุ่ม "SELECT INVOICE FOR SETTLEMENT"
2. เลือก Invoice ที่ต้องการรับเงิน
3. ระบุจำนวนเงินในคอลัมน์ "Paid"
4. กด Save
```

#### 2.2 ตรวจสอบ Withholding Tax (หัก ณ ที่จ่าย)
```
ถ้ามีการหัก ณ ที่จ่าย ให้กรอก:
✓ Department
✓ Account Code
✓ Total (ยอดเงิน)
✓ Rate (อัตราหัก %)
✓ Amount (ยอดหัก)
```

#### 2.3 ตรวจสอบ Advance Deposit
```
ถ้าลูกค้าจ่ายล่วงหน้า:
1. สร้าง Receipt โดยไม่ต้องเลือก Invoice
2. ใช้ "Apply Invoice for Advance Deposit" เพื่อนำมันตัดจ่ายภายหลัง
3. ตรวจสอบ "Credit Available" เพื่อดูยอดคงเหลือ
```

---

## 3. สร้างใบกำกับภาษีไม่ได้

### ปัญหา:
- สำหรับบริการ ไม่สามารถสร้างใบกำกับภาษีจาก Invoice ได้
- ภาษีสินค้า vs ภาษีบริการต่างกัน

### Solutions:

```
สินค้า (Goods):
→ ตั้งค่า Tax Status เป็น "Output Vat" ใน Invoice
→ ออกใบกำกับภาษีพร้อมกับ Invoice

บริการ (Services):
→ ตั้งค่า Tax Status เป็น "None" ใน Invoice
→ ออกใบกำกับภาษีเมื่อรับเงิน (Receipt)
→ ใน Receipt ให้ติ๊ก "Tax Invoice"
```

---

## 4. PMS Interface / City Ledger ไม่ทำงาน

### Error Messages:
- "Incomplete Data"
- "Mapping not found"
- "Cannot post from PMS"

### Solutions:

#### 4.1 ตรวจสอบ Mapping ระหว่าง PMS และ AR
```
วิธีที่ 1: Mapping ในระบบ
1. เข้าไปที่รายการ PMS Guest / Credit Card
2. Click ปุ่ม Edit
3. เลือก A/R Profile ที่ต้องการ Mapping
4. กด Save

วิธีที่ 2: Mapping ผ่าน Excel
1. Download CSV ของข้อมูล PMS
2. Edit ใน Excel โดยระบุ A/R No
3. Import กลับเข้าระบบ
```

#### 4.2 ตรวจสอบ Account Code สำหรับ PMS Posting
```
Setting → PMS Interface → Account Code Setup
ตรวจสอบว่ามี:
✓ Dr. Acc. Code (บัญชีเดบิต)
✓ Cr. Acc. Code (บัญชีเครดิต)
✓ Tax Account (บัญชีภาษี)
✓ Tax Type (Add/Include/None)
✓ Tax Rate (%)
```

---

## 5. Contract Application ไม่สำเร็จ

### Error Messages:
- "Contract already applied"
- "No active contract found"
- "Contract expired"

### Solutions:

```
1. ตรวจสอบสถานะ Contract ต้องเป็น "Active"
2. ตรวจสอบ Start Date และ End Date ว่าอยู่ในช่วงที่ใช้งาน
3. ตรวจสอบ "Charge Every Month" ตั้งค่าถูกต้อง
4. ไปที่ Function > Procedure > Apply Contract
5. เลือก Contract ที่ต้องการ Apply
6. ถ้ามีการ Apply ไปแล้ว → เลือก Replace ถ้าต้องการเปลี่ยน
```

---

## 6. ปัญหา Exchange Rate (อัตราแลกเปลี่ยน)

### ปัญหา:
- ยอดเงินในสกุลเงินต่างประเทศไม่ตรงกัน
- Exchange Gain/Loss คำนวณไม่ถูกต้อง

### Solutions:

```
1. ตรวจสอบ Rate ใน Invoice / Receipt
2. ตรวจสอบ Settlement Base Amount ใน Receipt
3. ตั้งค่า Gain/Loss Account ใน Configuration:
   - Configuration → Receipt → Gain Account
   - Configuration → Receipt → Loss Account
4. ตรวจสอบ Bank Charge Account (ถ้ามีค่าธรรมเนียม)
```

---

## 7. ปิด Period ไม่ได้

### Error Messages:
- "Cannot close period"
- "There are unposted transactions"
- "Period is locked"

### Solutions:

#### 7.1 ตรวจสอบ Transaction ที่ค้างอยู่
```
1. ตรวจสอบ AR Invoice ที่ยังไม่ได้บันทึก
2. ตรวจสอบ Receipt ที่ยังไม่ได้ทำ
3. ให้ทำรายการที่ค้างอยู่ก่อนปิดงวด
```

#### 7.2 ตรวจสอบ Posting Status
```
GL Module → Journal Voucher
ดูว่า AR Posting ไปยัง GL แล้วหรือยัง
ถ้ายังไม่ → ทำ Posting from AR ก่อน
```

#### 7.3 ขอ Permission จาก Admin
```
ถ้าแจ้งว่ารายการเรียบร้อยแต่ปิดไม่ได้
อาจจะถูก Lock โดย Admin หรือ User อื่น
ติดต่อ Admin เพื่อขอ Unlock Period
```

---

## 8. A/R Profile ไม่สามารถแก้ไข

### Causes:
- ลูกค้ามีการใช้งานอยู่ (มี Invoice หรือ Receipt)
- ลูกค้าถูก Lock โดย Admin
- User ไม่มีสิทธิ์ Edit

### Solutions:

```
1. ตรวจสอบว่า A/R Profile มีรายการค้างอยู่หรือไม่
2. ถ้ามี → ติดต่อ Admin เพื่อขอ Permission แก้ไข
3. หรือสร้าง A/R Profile รายการใหม่แทน
```

---

## 9. Credit Memo (CN) สร้างไม่ได้

### Solutions:

```
วิธีสร้าง Credit Memo:
1. สร้าง Invoice ใหม่
2. ใส่ยอดเป็นค่าลบ (Negative Amount)
3. ระบุรายละเอียดสาเหตุที่ Cut
4. บันทึกปกติ
5. ระบบจะนำค่าลบไปชำระกับยอดลูกค้า
```

---

## Quick Checklist ก่อนแจ้งปัญหา

```
[ ] ตรวจสอบ A/R Profile มีอยู่ในระบบ
[ ] ตรวจสอบ Account Code ถูกต้อง
[ ] ตรวจสอบ Invoice Date และ Due Date ถูกต้อง
[ ] ตรวจสอบยอด Dr = Cr ก่อนบันทึก
[ ] ตรวจสอบ Tax Status ถูกต้อง (สินค้า vs บริการ)
[ ] ตรวจสอบ Internet Connection เชื่อมต่ออยู่
```

---

## ติดต่อ Support

หากทำตามขั้นตอนแล้วยังไม่หาย:

1. **Screenshot Error** ที่แสดง
2. **ระบุ Module:** AR Module
3. **ระบุ Function:** สร้าง Invoice / รับเงิน / Reconciliation
4. **ระบุขั้นตอนที่ทำแล้ว** (Steps taken)
5. **ติดต่อ Admin:** แจ้งระบบลูกค้า
