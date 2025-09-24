---
title: Purchase Request
lang: th-TH
---
# Troubleshoot Guide PR
## กดApproved PR ไม่ได้ แก้ไขอย่างไร
ตัวอย่าง PR24020004 กดเข้ามาแล้วไม่พบปุ่มปุ่ม Approved/Reject/Send Back ให้กด
![alt text](image-146.png)

สาเหตุเกิดจากอยู่ในหัวข้อ View All ทำให้ไม่สามารถแก้ไขได้
![alt text](image-147.png)

ไปที่หัวข้อ View  หรือตามView Step เอกสารPR ของลูกค้า
![alt text](image-148.png)

ทำการคลิกที่PR24020004หรือหมายเลขPR ของลูกค้า
![alt text](image-149.png)


จะพบว่าปุ่ม Approved/Reject/Send Back ปรากฏขึ้นมาแล้วตามรูปภาพ
![alt text](image-150.png)

## Approve PR ช้า

ตัวอย่าง กด Approve PR25060001 ช้าผิดปกติ
![alt text](image-151.png)

สาเหตุ มีการตั่งค่า Web & Mail Server แต่ Mail Server ไม่สามารถส่งEmail ได้และมีการเลือก Receive Notification Via Email ในหัวข้อการ Approved ใน Workflow Configuration 

Solution:

1.ไปที่ Options> System Setting>Web & Mail Server 

2.ทดสอบ กดปุ่มTest sending PR/SR หรือ PO เพื่อดูว่าระบบสามารถส่งEmail ได้หรือไม่

จากตัวอย่าง พบError : (400) Bad Request.
![alt text](image-152.png)

3.ให้ทำการแก้ไข Setting Mail Server ให้ถูกต้อง ก็จะสามารถแก้ไขการ Approve ช้า ได้ครับซึ่งสามารถดูได้ที่
คู่มือการตั่งค่าMail Setting
![alt text](image-153.png)
 

## PR 1ใบ Gen PO ได้ 2 PO

ตัวอย่าง PR25080007 Gen แล้วได้ PO 2 ใบ คือ PO25080001 และ PO25080002
![alt text](image-154.png)

สาเหตุเกิดจาก มี Delivery on 2 วัน คือ 20/08/2025 และ 21/08/2025 ทำให้ระบบแยกเป็น2 PO
ระบบจับจาก Vendor และ Delivery on 
![alt text](image-155.png)

Solution: ไม่สามารถรวมเป็น 1 PO ได้เนื่องจากระบบจับจาก Vendor และ Delivery on หากต้องการรวมต้องแก้ไข Delivery on และ Close PO และทำ PR ใบใหม่ครับ


