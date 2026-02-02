---
title: "AP Module Troubleshooting"
title_en: "Account Payable Troubleshooting Guide"
lang: th-TH
module: carmen_cloud
submodule: ap
doc_type: troubleshooting
complexity: intermediate
tags: [ap, troubleshooting, error, account_payable]
country_specific: generic
target_audience: accountant
---

# Account Payable - แก้ปัญหา (Troubleshooting Guide)

## ปัญหาที่พบบ่อย (Common Issues)

---

## 1. บันทึก AP Invoice ไม่สำเร็จ

### Error Messages:
- "Cannot save invoice"
- "Vendor not found"
- "Account code is required"
- "Total Dr ≠ Cr"

### Solutions:

#### 1.1 ตรวจสอบข้อมูลบังคับท้องกรอก
```
✓ Invoice No (เลขที่ใบแจ้งหนี้)
✓ Vendor (รหัสเจ้าหนี้)
✓ Currency (สกุลเงิน)
✓ Invoice Date (วันที่ใบแจ้งหนี้)
✓ Invoice Detail (รายการสินค้า/บริการ อย่างน้อย 1 รายการ)
```

#### 1.2 ตรวจสอบ Account Code
```
Dr Acc Code → รหัสบัญชีค่าใช้จ่าย (เช่น ค่าใช้จ่าย, ซื้อ)
Cr Acc Code → รหัสบัญชีเจ้าหนี้การค้า
```

#### 1.3 ตรวจสอบ Tax Status
```
Confirm → ได้รับใบกำกับภาษีแล้ว (บันทึก Dr. ภาษีซื้อ)
Pending → ยังไม่ได้รับใบกำกับภาษี (บันทึก Dr. ภาษีซื้อตั้งพักไว้)
Unclaim → ใบกำกับภาษีที่ไม่สามารถขอคืนได้
None → ไม่มีภาษี
```

---

## 2. กด Payment ไม่ได้ / Payment Error

### Error Messages:
- "Insufficient balance"
- "Vendor balance is zero"
- "Cannot post to GL"

### Solutions:

#### 2.1 ตรวจสอบยอดเงิน Vendor
```
AP Module → Vendor Profile → ดูยอดเงินคงเหลือ
ถ้าไม่พอ → ติดต่อแผนก Accounts หรือ เพิ่มเครดิตเงิน
```

#### 2.2 ตรวจสอบ AP Invoice ที่จ่าย
```
ต้องลงหนี้ที่ยังไม่จ่าย (Unpaid Invoice) เท่านั้น
Invoice ที่ Paid หรือ Void แล้วจะแสดงไม่่ให้เลือก
```

#### 2.3 ตรวจสอบ Bank Account
```
Configuration → Payment Type → Bank Account
ตรวจสอบว่ามีบัญชีธนาคารที่จะใช้จ่ายเงิน
```

---

## 3. Input Tax Reconciliation ไม่ตรงกัน

### ปัญหา:
- ยอดภาษีซื้อในระบบไม่ตรงกับใบกำกับภาษี
- รายการที่ Mark Confirm แต่ยังไม่ได้รับใบกำกับภาษีจริง
- ยอดภาษีหัก ณ ที่จ่ายไม่ถูกตัด

### Solutions:

#### 3.1 ตรวจสอบรายการที่ Mark Pending
```
Input Tax Reconciliation → ติ๊กรายการที่ได้รับใบกำกับภาษีแล้ว
→ กด Confirm เพื่อย้ายอดเข้ารายงานภาษีซื้อ
```

#### 3.2 ตรวจสอบยอดภาษีหัก ณ ที่จ่าย
```
AP Invoice → ดู Tax Amount 2 และ Withholding Tax
→ ตรวจสอบว่าถูกหักออกจาก Payment แล้วหรือไม่
→ ถ้าใช่ → ตัดจากยอดใน Invoice ที่จ่าย
```

#### 3.3 Re-run Input Tax Reconciliation
```
หลังแก้ไขแล้วให้กด Recalculate หรือ
ลบรายการที่ Reconcile แล้วทำใหม่
```

---

## 4. Withholding Tax Reconciliation Error

### ปัญหา:
- ข้อมูลไม่ถูกส่งไป RDPrep
- ฟอร์มภาษีไม่ถูกต้อง
- แก้ไขข้อมูลแล้วแต่ยัง Error อยู่

### Solutions:

#### 4.1 ตรวจสอบ Form ที่เลือก
```
ภ.ง.ด. 3 → ใบแจ้งหนี้ / ค่าบริการ
ภ.ง.ด. 53 → หัก ณ จ่าย / เงินเดือน
ภ.ง.ด. 54 → หัก ณ จ่าย อื่น ๆ

ให้ตรวจสอบว่าเลือกฟอร์มถูกต้อง
```

#### 4.2 ตรวจสอบการเชื่อมต่อ RDPrep
```
1. เปิดโปรแกรม RDPrep
2. ตรวจสอบ Connection ไปยัง Revenue Department
3. ทดสอบส่งข้อมูล Test 1-2 รายการก่อน
4. ถ้า Error → ติดต่อ IT Support
```

---

## 5. ปิด Period ไม่ได้

### Error Messages:
- "Cannot close period"
- "There are unposted transactions"
- "Period is locked"

### Solutions:

#### 5.1 ตรวจสอบ Transaction ที่ค้างค้างอยู่
```
1. ตรวจสอบ AP Invoice ที่ยังไม่ได้บันทึก
2. ตรวจสอบ Payment ที่ยังไม่ได้ทำ
3. ให้ทำรายการที่ค้างค้างอยู่ก่อปิดงวด
```

#### 5.2 ตรวจสอบ Posting Status
```
GL Module → Journal Voucher
ดูว่า AP Posting ไปยัง GL แล้วหรือยัง
ถ้ายังไม่ → ทำ Posting from AP ก่อน
```

#### 5.3 ขอ Permission จาก Admin
```
ถ้าแจ้งว่ารายการเรียบร้อยแล้วแต่ปิดไม่ได้
อาจจะถูก Lock โดย Admin หรือ User อื่น
ติดต่อ Admin เพื่อขอ Unlock Period
```

---

## 6. Vendor Profile ไม่สามารถแก้ไข

### Causes:
- Vendor มีการใช้งานอยู่ (มี Invoice หรือ Payment)
- Vendor ถูก Lock โดย Admin
- User ไม่มีสิทธิ์ Edit

### Solutions:

```
1. ตรวจสอบว่า Vendor มีรายการค้างอยู่หรือไม่
2. ถ้ามี → ติดต่อ Admin เพื่อขอ Permission แก้ไข
3. หรือสร้าง Vendor รายการใหม่แทน
```

---

## 7. Deposit ไม่หักลบจาก Invoice อัตโนมัติ

### Solutions:

```
1. เปิด AP Invoice ที่เกี่ยวข้องกับ Deposit
2. Click เลือก "Apply Deposit" หรือ "Apply Deposit to Invoice"
3. เลือก Deposit ที่ต้องการนำมาหัก
4. ระบุจำนวนเงินที่ต้องการหัก
5. กด Save
```

---

## Quick Checklist ก่อนแจ้งปัญหา

```
[ ] รู้จักทำอย่าง (ควรทำอะไรก่อนแจ้งปัญหา)
[ ] ตรวจสอบ Vendor มีอยู่ในระบบ
[ ] ตรวจสอบ Account Code ถูกต้อง
[ ] ตรวจสอบ Invoice Date และ Due Date ถูกต้อง
[ ] ตรวจสอบยอด Dr = Cr ก่อบันทึก
[ ] ตรวจสอบ Internet Connection เชื่อมต่ออยู่
```

---

## ติดต่อ Support

หากทำตามขั้นตอนแล้วยังไม่หาย:

1. **Screenshot Error** ที่แสดง
2. **ระบุ Module:** AP Module
3. **ระบุ Function:** สร้าง Invoice / จ่ายเงิน / Reconciliation
4. **ระบุขั้นตอนที่ทำแล้ว** (Steps taken)
5. **ติดต่อ Admin:** แจ้งระบบลูกค้า
