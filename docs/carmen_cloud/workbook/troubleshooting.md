---
title: "Carmen Workbook Troubleshooting"
title_en: "Carmen Workbook Troubleshooting Guide"
lang: th-TH
module: carmen_cloud
submodule: workbook
doc_type: troubleshooting
complexity: intermediate
tags: [workbook, troubleshooting, excel, add-in, error]
country_specific: generic
target_audience: accountant
---

# Carmen Workbook - คู่มือแก้ปัญหา (Troubleshooting Guide)

## ปัญหาที่พบบ่อย (Common Issues)

---

## 1. กดปุ่ม Refresh ไม่ได้ / Refresh Button Not Working

### สาเหตุ (Causes)

| สาเหตุ | คำอธิบาย |
|---------|-----------|
| ไฟล์ Excel ยังไม่ถูก Unblock | Windows บล็อกไฟล์ที่ดาวนโหลดมา |
| Carmen Add-in ยังไม่ได้เปิดใช้งาน | Add-in ถูก disabled หรือยังไม่ได้ติดตั้ง |
| การเชื่อมต่อ Internet ไม่ได้ | ไม่สามารถดึงข้อมูลจากระบบ |
| Macro ยังไม่ได้เปิดใช้งาน | Excel Security บล็อก Macro |

### วิธีแก้ไข (Solutions)

#### Solution 1.1: Unblock ไฟล์ Excel (สำคัญที่สุด)

```
1. Click ขวาที่ไฟล์ Excel
2. เลือก Properties
3. ติ๊กถูก "Unblock" ที่ข้างล่าง
4. กด Apply
5. กด OK
6. ปิดและเปิดไฟล์ Excel ใหม่
```

**ภาพประกอบ:**
```
[General] Security
□ Unblock

Apply  OK  Cancel
```

#### Solution 1.2: ตรวจสอบ Carmen Add-in ถูกเปิดใช้งาน

```
1. เปิด Excel > File > Options
2. เลือก Add-Ins
3. ที่ "Manage:" เลือก "Excel Add-ins" > กด Go
4. ตรวจสอบว่า "Carmen Excel Add-In" มี ✅ ถูกติ๊ก
5. ถ้าไม่มี ให้ทำการติดตั้งใหม่
```

#### Solution 1.3: เปิดใช้งาน Macro

```
1. File > Options > Trust Center
2. Trust Center Settings > Macro Settings
3. เลือก "Enable all macros" หรือ "Enable VBA macros"
4. ติ๊ก "Enable Excel 4.0 macros when VBA macros are enabled"
5. กด OK
```

#### Solution 1.4: ทดสอบ Connection

```
1. ไปที่ Tab "Carmen Add-In"
2. กด "Config WebAPI"
3. กด "Login" ใส่ username/password
4. ถ้า Login สำเร็จ = เชื่อมต่อได้
5. ถ้า Error = ติดต่อ Support
```

---

## 2. ปุ่ม/ฟังก์ชัน Carmen Add-in ไม่แสดง

### Solution 2.1: ติดตั้ง Add-in ใหม่

```
1. ดาวนโหลด Excel Add-In จาก: https://xxxxx.carmen.blue/carmen.api
2. เลือก x32 หรือ x64 ตามระบบปฏิบัติ
3. Double Click ไฟล์ที่ดาวนโหลด
4. กด Install และรอจนเสร็จ
5. รีสตาร์ท Excel
```

---

## 3. Error เมื่อกด Refresh / Connection Error

### ข้อความแสดง:

| Error | สาเหตุ |
|-------|---------|
| "Connection Failed" | ไม่สามารถเชื่อมต่อ Server |
| "Login Failed" | Username/Password ผิด หรือ User ถูกระงับ |
| "Timeout" | อินเทอร์เน็ตช้ายหรือ Server ล่ม |
| "Unauthorized" | ไม่มีสิทธิ์เข้าถึง Business Unit |

### Solution:

```
1. ตรวจสอบ Internet Connection
2. ทดสอบ Login ใหม่ (Config WebAPI > Login)
3. ติดต่อ Admin เพื่อตรวจสอบ User Permission
4. ลองกด Recalculate All Sheets แทน Refresh
```

---

## 4. ข้อมูลไม่อัปเดตหลัง Refresh

### Solution 4.1: ตรวจสอบ Business Unit

```
1. ไปที่ Sheet "Parameters"
2. ดูว่า BU ที่ต้องการแสดงอยู่ในรายการหรือไม่
3. ถ้าไม่มี = ติดต่อ Admin เพื่อขอ Permission
4. กด "Recalculate All Sheets" อีกครั้ง
```

### Solution 4.2: เช็ค Filters

```
1. ตรวจสอบว่ามีการ Filter ข้อมูลอยู่หรือไม่
2. Clear Filter ทั้งหมด
3. กด Refresh ใหม่
```

---

## 5. ไฟล์ Excel ขึ้น Error "Protected View"

### Solution 5.1:

```
1. กด "Enable Editing" สีเหลืองด้านบน
2. ถ้ายังไม่ได้ → ตรวจสอบ Trust Center access
```

---

## 6. Performance Issue - เปิดไฟล์ช้ามาก

### Solution 6.1:

```
1. ตรวจสอบขนาดไฟล์ (ถ้าใหญ่ > 5MB อาจช้า)
2. ลบข้อมูลเก่าที่ไม่ใช้ใน Sheet
3. ปิดฟังก์ชัน Automatic Calculation ชั่วคราง
   - Formulas > Calculation Options > Manual
4. กด Recalculate เฉพาะตอนต้องการ
```

---

## 7. Cannot Upload Transaction (JV, Budget)

### Solution 7.1:

```
1. ตรวจสอบ Connection Status (ต้อง Login อยู่)
2. ตรวจสอบว่า Business Unit ถูกต้อง
3. ตรวจสอบ Required Fields ครบถ้วน
4. ดู Error Message ที่แสดงใน Status Column
```

---

## Quick Reference - Checklist ก่อนแจ้งปัญหา

ก่อนแจ้งปัญหา ให้ตรวจสอบ:

```
[ ] ไฟล์ Excel ถูก Unblock แล้ว
[ ] Carmen Add-in ถูกเปิดใช้งาน
[ ] Macro Settings ถูกเปิดใช้งาน
[ ] Login เข้าระบบสำเร็จ
[ ] Internet เชื่อมต่อได้
[ ] Business Unit ถูกต้อง
[ ] กด Recalculate All Sheets แล้ว
```

---

## ติดต่อ Support

หากทำตามขั้นตอนแล้วยังไม่หาย:

1. **Screenshot Error** ที่แสดง
2. **ระบุ Excel Version** (2016, 2019, 365, etc.)
3. **ระบุ Windows Version** (10, 11, etc.)
4. **ระบุขั้นตอนที่ทำแล้ว** (Steps taken)
5. **ติดต่อ Admin:** แจ้งระบบลูกค้า (xxxxx@carmen.blue)

---

## เอกสารที่เกี่ยวข้อง (Related Documents)

- [WB-install&config](./WB-install&config.md) - วิธีติดตั้งและตั้งค่า
- [WB-function](./WB-function.md) - ฟังก์ชันการใช้งาน
- [Carmen Support](https://xxxxx.carmen.blue) - คู่มือออนไลน์
