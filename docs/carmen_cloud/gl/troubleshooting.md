---
title: "GL Module Troubleshooting"
title_en: "General Ledger Troubleshooting Guide"
lang: th-TH
module: carmen_cloud
submodule: gl
doc_type: troubleshooting
complexity: intermediate
tags: [gl, troubleshooting, error, general_ledger, journal_voucher]
country_specific: generic
target_audience: accountant
---

# General Ledger - แก้ปัญหา (Troubleshooting Guide)

## ปัญหาที่พบบ่อย (Common Issues)

---

## 1. บันทึก Journal Voucher (JV) ไม่สำเร็จ

### Error Messages:
- "Dr ≠ Cr" (Debit/Credit imbalance)
- "Cannot save voucher"
- "Account code is required"
- "Total amount is zero"

### Solutions:

#### 1.1 ตรวจสอบ Dr = Cr
```
ทุก JV ต้องมีอย่างน้อย 2 รายการ
รายการละเอียด (Detail) อย่างน้อย 1 Debit และ 1 Credit

Total Debit Amount = Total Credit Amount

ถ้าไม่เท่ากัน → ระบบจะไม่ให้บันทึก
```

#### 1.2 ตรวจสอบ Required Fields
```
✓ Voucher Date (วันที่บันทึก)
✓ Account Code (รหัสบัญชี)
✓ Description (รายละเอียด)
✓ Debit หรือ Credit Amount
✓ Department (รหัสแผนก)
```

#### 1.3 ตรวจสอบ Period
```
ถ้า Period ถูกปิดไปแล้ว → ไม่สามารถบันทึก JV ได้
ต้องสร้าง JV ใน Period ปัจจุบัน
```

---

## 2. Copy JV แล้ว Save ไม่ได้

### ปัญหา:
- กด Copy → "Copy to new JV with zero amount" แล้ว Save ไม่ได้

### Solutions:

```
เมื่อ Copy ด้วย "zero amount":
1. ระบบสร้าง JV ใหม่พร้อมรายการทั้งหมด
2. แต่ Amount = 0 ทั้งหมด
3. ต้องกรอกจำนวนเงินใหม่ในทุกบรรทัด
4. ตรวจสอบให้มั่นใจว่า Dr = Cr
5. จากนั้นจึงจะ Save ได้
```

---

## 3. แก้ไข JV ที่ Posted แล้วไม่ได้

### ปัญหา:
- แก้ไข JV ที่ Posted แล้วไม่ได้
- ปุ่ม Edit ไม่สามารถกดได้
- JV ไม่สามารถเปิดแก้ไขได้
- แก้ไข JV ที่โพสต์แล้ว ไม่ได้
- Edit posted JV cannot
- แก้ไข JV ที่ Posted แล้วได้ไหม
- แก้ไข JV โพสต์แล้ว ได้ไหม

### สาเหตุ:
เมื่อ JV ถูก Posted แล้ว → ระบบจะ Lock ไม่ให้แก้ไข เพื่อรักษาความถูกต้องของบัญชี

### Solutions:

#### วิธีแก้ไขที่ถูกต้อง:
```
แก้ไข JV ที่ Posted แล้วได้ไหม -> ไม่ได้ แต่สามารถทำ Reversal ได้

วิธีแก้ไข:
1. ค้นหา JV ตัวเดิมที่ Posted แล้ว
2. Click ปุ่ม Copy → "Copy and reverse transaction"
3. ระบบสร้าง JV ตัวกลับ (Reversal JV)
4. สร้าง JV ตัวใหม่ที่ถูกต้องแทน
5. บันทึก (Save) และ Post JV ตัวใหม่

ผลลัพธ์:
- JV ตัวเดิมยังคงอยู่ (เพื่อเป็นประวัติ)
- JV ตัวกลับ (Reversal) ยกเลิก JV ตัวเดิม
- JV ตัวใหม่บันทึกรายการที่ถูกต้อง
```

#### 3.2 ตรวจสอบ Period
```
ถ้า Period ถูกปิดแล้ว:
- แก้ไข JV ตัวเดิมไม่ได้
- สร้าง JV ตัวใหม่ใน Period ปัจจุบันเพื่อแก้ไข
- หรือติดต่อ Support เพื่อขอเปิด Period (ต้องแจ้ง FC หรือ Account Manager)
```

---

## 4. Posting จาก Module อื่นไม่สำเร็จ

### Error Messages:
- "Cannot post to GL"
- "Invalid date range"
- "No data to post"

### Solutions:

#### 4.1 ตรวจสอบ Date Range
```
From Date ต้องน้อยกว่าหรือเท่ากับ To Date
ถ้า From > To → ระบบจะไม่ให้ Post
```

#### 4.2 ตรวจสอบลำดับการ Posting
```
ลำดับที่ถูกต้อง:
1. Inventory Module (COGS / Extra Cost)
2. AP Module (AP Invoice / AP Payment)
3. AR Module (AR Invoice / AR Receipt)
4. Asset Module (Depreciation / Disposal)

หลังจาก Source Module แล้ว → ค่อย Post ไป GL
```

#### 4.3 ตรวจสอบ Account Mapping
```
Configuration → Account Code Mapping
ตรวจสอบว่าแต่ละ Module มี Account Code ครบ:
- Dr. Account Code
- Cr. Account Code
- Tax Account (ถ้ามี)
- Gain/Loss Account (ถ้ามี)
```

---

## 5. ปิด Period ไม่ได้

### Error Messages:
- "Cannot close period"
- "There are unposted transactions"
- "Other modules not closed"

### Solutions:

#### 5.1 ตรวจสอบ Module Periods
```
ก่อนปิด GL Period ต้องปิด Module อื่นก่อน:
[ ] AP Period
[ ] AR Period
[ ] Asset Period
[ ] Inventory Period

หลังจากปิดทั้งหมดแล้ว → ค่อยปิด GL Period
```

#### 5.2 ตรวจสอบ Unposted Transactions
```
1. ตรวจสอบ JV ที่ยังไม่ Posted
2. ตรวจสอบ Posting จาก Module อื่น
3. ให้ทำรายการที่ค้างอยู่ก่อนปิดงวด
```

#### 5.3 ขอ Permission จาก Admin
```
ถ้าแจ้งว่ารายการเรียบร้อยแล้วแต่ปิดไม่ได้
ติดต่อ FC หรือ Account Manager
เพื่อขอ Unlock Period หรือตรวจสอบสิทธิ์
```

---

## 6. Template Voucher ใช้งานไม่ได้

### ปัญหา:
- Template ไม่แสดงใน Dropdown
- Apply Template แล้วข้อมูลไม่ถูกต้อง

### Solutions:

```
1. ตรวจสอบว่า Template มีอยู่จริงใน Template Voucher Module
2. ตรวจสอบ Prefix ของ Template ตรงกับ Prefix ที่เลือกหรือไม่
3. สร้าง Template:
   วิธีที่ 1: สร้างใหม่ใน Template Voucher
   วิธีที่ 2: Copy จาก JV ที่มีอยู่ → Save เป็น Template
4. ใช้ Template:
   - สร้าง JV ใหม่
   - กดปุ่ม Template
   - เลือก Template ที่ต้องการ
   - แก้ไขจำนวนเงิน (ถ้าต้องการ)
```

---

## 7. Recurring Voucher ไม่ทำงาน

### ปัญหา:
- Apply Recurring Template แล้วไม่เกิด JV
- สร้าง Recurring แล้วไม่ทำงานตามกำหนด

### Solutions:

```
1. ตรวจสอบ From Date และ To Date ของ Recurring Template
2. ตรวจสอบว่า Period ที่เลือก Apply อยู่ในช่วงวันที่
3. ตรวจสอบ Frequency (รายเดือน / รายไตรมาส / อื่นๆ)
4. ไปที่ Function → Procedure → Apply Recurring Template
5. เลือก Period และ Template ที่ต้องการ
6. กด Apply
```

---

## 8. Financial Report แสดงยอดไม่ถูกต้อง

### ปัญหา:
- บัญชีไม่แสดงในรายงาน
- ยอดเงินเป็นบวกแต่ควรเป็นลบ หรือกลับกัน

### Solutions:

#### 8.1 Map Account ไปยัง Financial Report
```
1. เปิด Financial Report (Balance Sheet / P&L)
2. Click ปุ่ม Setting (รูปฟันเฟือง)
3. Map Account Code ไปยัง Section ที่ต้องการ
4. กด Save
```

#### 8.2 ตั้งค่า Reverse Sign
```
สำหรับบัญชีที่ควรแสดงกลับลำ (Contra Account):
1. เข้าไป Chart of Accounts
2. เลือก Account Code ที่ต้องการ
3. ติ๊ก "Reverse Sign"
4. กด Save

หมายเหตุ: Reverse Sign ส่งผลต่อ GL Financial Reports เท่านั้น
```

---

## 9. Budget ไม่แสดงในรายงาน

### ปัญหา:
- เปรียบเทียบ Actual vs Budget ไม่ได้
- Budget แสดง 0 ทั้งหมด

### Solutions:

```
1. ตรวจสอบว่ามีการตั้งค่า Budget แล้ว:
   - Budget Module → Enter Budget
   - เลือก Department
   - เลือก Account Code
   - กรอก Budget รายเดือน

2. ตรวจสอบ Budget Revision:
   - สามารถแก้ไขได้ถึง 4 Revisions
   - เลือก Revision ที่ต้องการใช้งาน

3. ใน Profit & Loss Report:
   - เลือก Show Budget
   - เลือก Revision ที่ต้องการ
```

---

## Quick Checklist ก่อนแจ้งปัญหา

```
[ ] ตรวจสอบ Dr = Cr ก่อนบันทึก
[ ] ตรวจสอบ Account Code ถูกต้อง
[ ] ตรวจสอบ Voucher Date อยู่ใน Period ที่เปิดอยู่
[ ] ตรวจสอบ JV Posted แล้วหรือยัง
[ ] ตรวจสอบ Module Periods ปิดครบหรือยัง
[ ] ตรวจสอบ Internet Connection เชื่อมต่ออยู่
```

---

## ติดต่อ Support

หากทำตามขั้นตอนแล้วยังไม่หาย:

1. **Screenshot Error** ที่แสดง
2. **ระบุ Module:** GL Module
3. **ระบุ Function:** สร้าง JV / Posting / Report
4. **ระบุขั้นตอนที่ทำแล้ว** (Steps taken)
5. **ติดต่อ Admin:** แจ้งระบบลูกค้า
