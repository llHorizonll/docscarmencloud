---
title: "Configuration Module Troubleshooting"
title_en: "Configuration Module Troubleshooting Guide"
lang: th-TH
module: carmen_cloud
submodule: configuration
doc_type: troubleshooting
complexity: intermediate
tags: [configuration, troubleshooting, error, setup, user_permission]
country_specific: generic
target_audience: system_admin
---

# Configuration Module - แก้ปัญหา (Troubleshooting Guide)

## ปัญหาที่พบบ่อย (Common Issues)

---

## 1. ลบข้อมูล Configuration ไม่ได้

### Error Messages:
- กด Delete แล้วไม่มีอะไรเกิดขึ้น
- แสดงข้อความยืนยันแต่ข้อมูลไม่หายไป

### ปัญหาที่เกิดขึ้นได้:

| รายการ | สาเหตุ |
|---------|---------|
| Currency (สกุลเงิน) | ถูกใช้งานอยู่ในระบบ |
| Currency Exchange Rate | มีประวัติการใช้งาน |
| Department (แผนก) | มีการใช้งานอยู่ |
| Dimension | ถูกอ้างอิงโดยรายการอื่น |
| Payment Type | ถูกใช้ใน AP/AR |
| Unit (หน่วย) | ถูกใช้ในสินค้า/บริการ |
| Account Code (รหัสบัญชี) | **มีการบันทึกบัญชีแล้ว** |

### Solutions:

```
วิธีแก้ไขที่ถูกต้อง:
1. อย่าลบข้อมูลที่ถูกใช้งานแล้ว
2. เปลี่ยน Status เป็น "Inactive" แทน
3. ข้อมูลที่ Inactive จะไม่แสดงใน Dropdown ให้เลือก

ขั้นตอน:
1. เปิดรายการที่ต้องการ
2. เปลี่ยน Status: Active → Inactive
3. กด Save
4. กด OK เพื่อยืนยัน
```

---

## 2. Password ไม่ผ่านการตรวจสอบ

### Error Messages:
- "Invalid password"
- "Password does not meet requirements"

### Requirements:

```
Password ต้องมีความยาวอย่างน้อย 8 ตัวอักษร
และประกอบด้วย:

✓ ตัวอักษรภาษาอังกฤษ (a-z, A-Z)
✓ ตัวเลข (0-9)
✓ อักขระพิเศษ (!@#$%^&*()_+|~-=`{}[]:”;'<>?,./)

ตัวอย่าง Password ที่ถูกต้อง:
- Carmen@2024
- Pass#1234
- My$ecurePwd
```

---

## 3. แก้ไข Company Profile ไม่ได้

### ปัญหา:
- ฟิลด์ "Reg. Name" แก้ไขไม่ได้

### Solutions:

```
ฟิลด์ "Reg. Name" เชื่อมโยงกับ License
ไม่สามารถแก้ไขเองได้หลังจากตั้งค่าครั้งแรก

หากต้องการเปลี่ยน:
1. ติดต่อ Support
2. แจ้งเหตุผลและเอกสารสนับสนุน
3. รอการดำเนินการจากทีมงาน
```

---

## 4. เปลี่ยน Account Nature ไม่ได้

### ปัญหา:
- ฟิลด์ "Acc. Nature" แก้ไขไม่ได้
- Dropdown ถูก Disable
- เปลี่ยน Account Nature ได้ไหม
- Change account nature cannot

### สาเหตุ:
เมื่อมีการนำ Account Code ไปใช้ในการบันทึกบัญชีแล้ว
จะไม่สามารถแก้ไข หรือเปลี่ยน Acc. Nature ได้

### Solutions:

#### วิธีแก้ไขที่ถูกต้อง:
```
เปลี่ยน Account Nature ได้ไหม -> ไม่ได้ หลังจากใช้งานแล้ว

หมายเหตุ:
- เมื่อ Account Code ถูกนำไปใช้ในการบันทึกบัญชีแล้ว
- จะไม่สามารถแก้ไข หรือเปลี่ยน Account Nature ได้
- นี่คือข้อจำกัดของระบบเพื่อรักษาความถูกต้องของบัญชี

วิธีป้องกัน:
1. วางแผน Account Code และ Account Nature ให้ดีก่อนเริ่มใช้งาน
2. ทดสอบระบบด้วย Account Code ทดสอบก่อนใช้งานจริง
3. ตรวจสอบ Account Nature อีกครั้งก่อนบันทึกบัญชีครั้งแรก

Account Nature ทั้ง 5 หมวด:
หมวด 1 → สินทรัพย์ (Assets) → Dr.
หมวด 2 → หนี้สิน (Liabilities) → Cr.
หมวด 3 → ทุน (Equity) → Cr.
หมวด 4 → รายได้ (Revenue) → Cr.
หมวด 5 → ค่าใช้จ่าย (Expenses) → Dr.
```

---

## 5. User Permission ทำงานไม่ถูกต้อง

### ปัญหา:
- User ไม่เห็น Module ที่ควรจะเห็น
- User ทำรายการบางอย่างไม่ได้
- User เห็นทุกอย่าง (มากเกินไป)

### Solutions:

#### 5.1 ตรวจสอบ Module Permission
```
Administrator → User Permission
ตรวจสอบ Module ที่ User สามารถเข้าถึง:

[ ] Account Payable (AP)
[ ] Account Receivable (AR)
[ ] General Ledger (GL)
[ ] Asset Management
[ ] Administrator
[ ] Setting

ติ๊กถูกเฉพาะ Module ที่ User ควรเข้าถึง
```

#### 5.2 ตรวจสอบ Function Permission
```
แต่ละ Module มี Function ย่อย:
- View (ดูข้อมูล)
- Add (เพิ่มข้อมูล)
- Update (แก้ไขข้อมูล)
- Delete (ลบข้อมูล)

ใช้ปุ่มลูกศร (← →) เพื่อย้าย Function ระหว่าง:
- Available Function: ที่ยังไม่ได้ใช้งาน
- Assigned Function: ที่ User สามารถเข้าถึง
```

#### 5.3 ตรวจสอบ Business Unit Permission
```
User อาจมีสิทธิ์เข้าถึงบาง BU เท่านั้น
ตรวจสอบที่:
Administrator → User Profile → Business Unit
```

---

## 6. เลือก Account Code ผิดแผนก

### ปัญหา:
- User เลือก Account Code ที่ไม่ใช่ของแผนกตัวเอง
- ทำให้ Report ไม่ถูกต้อง

### Solutions:

```
ตั้งค่า "Select Account code" ใน Department:

1. Setting → Department
2. เลือก Department ที่ต้องการ
3. ที่ฟิลด์ "Select Account code"
4. เลือกเฉพาะ Account Code ที่เกี่ยวข้องกับแผนกนั้น
5. กด Save

ผล: เมื่อ User เลือก Department นั้น
ระบบจะแสดงเฉพาะ Account Code ที่กำหนดไว้
ช่วยป้องกันการเลือก Account code ผิดแผนก
```

---

## 7. Currency Exchange Rate ไม่อัปเดต

### ปัญหา:
- อัตราแลกเปลี่ยนเก่าเกินไป
- ไม่สามารถบันทึก Exchange Rate ใหม่

### Solutions:

```
1. ตรวจสอบว่า Currency ถูกสร้างแล้ว
   Setting → Currency
   ต้องมีสกุลเงินที่ต้องการก่อน

2. สร้าง Exchange Rate:
   Setting → Currency Exchange Rate
   - Currency Code: เลือกสกุลเงิน
   - Date: วันที่มีผล
   - Buying Rate: อัตราซื้อ
   - Selling Rate: อัตราขาย
   - Average Rate: อัตราเฉลี่ย

3. ระบบรองรับประวัติอัตราแลกเปลี่ยนรายวัน
   สามารถตรวจสอบย้อนหลังได้
```

---

## 8. Payment Type ใช้งานไม่ได้

### ปัญหา:
- Payment Type ไม่แสดงใน Dropdown
- เลือก Payment Type ไม่ได้

### Solutions:

```
1. ตรวจสอบ Status ของ Payment Type:
   Setting → Payment Type
   ต้องเป็น Active

2. ตรวจสอบ Account Code ที่เกี่ยวข้อง:
   - Bank Account (บัญชีธนาคาร)
   - Cash Account (บัญชีเงินสด)
   - Credit Account (บัญชีเครดิต)

3. สำหรับ Cheque:
   - ตั้งค่า Cheque Book
   - ระบุเลขที่เริ่มต้นและสิ้นสุด
```

---

## 9. Dimension / Unit ใช้งานไม่ได้

### ปัญหา:
- Dimension ไม่แสดงใน Transaction
- Unit ไม่แสดงใน Product

### Solutions:

```
Dimension:
1. Setting → Dimension
2. ตรวจสอบ Status = Active
3. ตรวจสอบว่ามีการเชื่อมโยงกับ Module ที่ใช้งาน

Unit:
1. Setting → Unit
2. ตรวจสอบ Status = Active
3. ตรวจสอบว่าถูกกำหนดให้ Product/Service
```

---

## 10. System Preferences ตั้งค่าไม่ได้

### รายการที่ Fix ไว้ (ไม่สามารถเปลี่ยนแปลง):

```
✓ Decimal Separator: . (จุด)
✓ Thousand Separator: , (ลูกน้ำ)
✓ Base Currency: THB (บาท)
✓ Date Format: DD/MM/YYYY

รายการที่สามารถตั้งค่าได้:
- Decimal Places for Amount (จำนวนทศนิยมสำหรับยอดเงิน)
- Decimal Places for Cost (จำนวนทศนิยมสำหรับต้นทุน)
- Decimal Places for Price (จำนวนทศนิยมสำหรับราคา)
- Decimal Places for Quantity (จำนวนทศนิยมสำหรับปริมาณ)
- Decimal Places for Rate (จำนวนทศนิยมสำหรับอัตรา)
```

---

## Quick Checklist ก่อนแจ้งปัญหา

```
[ ] ตรวจสอบว่าข้อมูลถูกใช้งานอยู่หรือไม่ (ก่อนลบ)
[ ] ตรวจสอบ Password ผ่านทุก Requirement
[ ] ตรวจสอบ Account Code มีการใช้งานแล้ว (ก่อนเปลี่ยน Nature)
[ ] ตรวจสอบ User Permission ถูกต้อง
[ ] ตรวจสอบ Status = Active (สำหรับ Configuration ที่ใช้งาน)
[ ] ติดต่อ Admin ก่อนแก้ไขข้อมูลสำคัญ
```

---

## ติดต่อ Support

หากทำตามขั้นตอนแล้วยังไม่หาย:

1. **Screenshot Error** ที่แสดง
2. **ระบุ Module:** Configuration Module
3. **ระบุ Function:** User Permission / Account Code / System Preferences
4. **ระบุขั้นตอนที่ทำแล้ว** (Steps taken)
5. **ติดต่อ Admin:** แจ้งระบบลูกค้า

---

## เอกสารที่เกี่ยวข้อง (Related Documents)

- [User Permission Guide](./user_permission.md) - การจัดการสิทธิ์ผู้ใช้
- [Account Setup Guide](./account_setup.md) - การตั้งค่าบัญชี
- [System Preferences](./system_preferences.md) - การตั้งค่าระบบ
