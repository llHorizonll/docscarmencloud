import { defineConfig } from "vitepress";

// https://vitepress.dev/reference/site-config
export default defineConfig({
  title: "CARMEN",
  description: "Document for carmen.blue",
  head: [["link", { rel: "icon", href: "/favicon.ico" }]],
  themeConfig: {
    // https://vitepress.dev/reference/default-theme-config
    nav: [
      { text: "Home", link: "/" },
      {
        text: "Changelog",
        items: [
          {
            text: "🆕 January2025 Relaese Infomation",
            link: "/jan2025",
          },
          {
            text: "November2024 Relaese Infomation",
            link: "/nov2024",
          },
          {
            text: "August2024 Relaese Infomation",
            link: "/aug2024",
          },
          {
            text: "June2024 Relaese Infomation",
            link: "/june2024",
          },
          {
            text: "May2024 Relaese Infomation",
            link: "/may2024",
          },
          {
            text: "Changelog",
            link: "/changelog/index",
            activeMatch: "/changelog/",
          },
        ],
      },
      // { text: "Examples", link: "/markdown-examples" },
    ],
    sidebar: {
      "/carmen_cloud/": { base: "/carmen_cloud/", items: sidebarAll() },
      "/training_center/": { base: "/training_center/", items: sidebarTraining() },
    },

    socialLinks: [{ icon: "github", link: "https://github.com/llHorizonll/docscarmencloud" }],
    search: {
      provider: "local",
    },
  },
  cacheDir: "./.vitepress/.vite",
});

function sidebarAll() {
  return [
      {
        text: "Dashboard",
        link: "/dashboard",
      },
      {
        text: "General Ledger",
        collapsed: true,
        base: '/carmen_cloud/gl/c-',
        items: [
          { text: "Journal Voucher", link: "journal_voucher" },
          { text: "Template Voucher", link: "template_voucher" },
          { text: "Recurring Voucher", link: "recurring_voucher" },
          { text: "Amortization Voucher", link: "amortization_voucher" },
          { text: "Allocation Voucher", link: "allocation_voucher" },
          { text: "Budget", link: "budget" },
          { text: "Posting Account Payable to GL", link: "posting_ap" },
          { text: "Posting Account Receivable to GL", link: "posting_ar" },
          { text: "Inventory & Extra Cost Posting to GL", link: "posting_inventory" },
          { text: "Posting Fixed Assets to GL", link: "posting_asset" },
          { text: "Close Period and Year End", link: "close_period" },
        ],
      },
      {
        text: "Account Payable",
        collapsed: true,
        base: '/carmen_cloud/ap/AP-',
        items: [
          { text: "Vendor", link: "vendor" },
          { text: "Posting AP invoice from recieving", link: "recevingToAp" },
          { text: "Invoice", link: "invoice" },
          { text: "Payment", link: "payment" },
          { text: "Deposit Payment", link: "deposit_payment" },
          { text: "Apply Deposit with Invoice", link: "apply_deposit_pay_with_inv" },
          { text: "Cheque Reconciliation", link: "cheque_reconciliation" },
          { text: "Input Tax Reconciliation", link: "input_tax_reconciliation" },
          { text: "WHT Reconciliation", link: "wht_reconciliation" },
          { text: "RDPrep_การโอนย้ายข้อมูลใบแนบ ภงด 3", link: "RDPrep_3" },
          { text: "RDPrep_การโอนย้ายข้อมูลใบแนบ ภงด 53", link: "RDPrep_53" },
          { text: "Close Period AP", link: "close_period" },
        ],
      },
      {
        text: "Account Receivable",
        collapsed: true,
        base: '/carmen_cloud/ar/AR-',
        items: [
          { text: "Profile", link: "profile" },
          { text: "AR Posting from PMS (PMS Interface)", link: "posting_pms" },
          { text: "Folio", link: "folio" },
          { text: "Invoice", link: "invoice" },
          { text: "Contract", link: "contract" },
          { text: "Apply AR Contract", link: "apply_contract" },
          { text: "Receipt", link: "receipt" },
          { text: "Receipt for Advance Deposit", link: "receipt_advance_deposit" },
          { text: "Apply invoice for Advance Deposit", link: "apply_invoice_advance_deposit" },
          { text: "Close Period AR", link: "close_period" },
        ],
      },
      {
        text: "Asset",
        collapsed: true,
        base: '/carmen_cloud/asset/AS-',
        items: [
          { text: "Pre-Register Asset Setting", link: "preasset_setting" },
          { text: "Pre-Register Asset", link: "preasset" },
          { text: "Asset Register", link: "asset_register" },
          { text: "Print Asset QR Code", link: "print_asset" },
          { text: "Asset Disposal", link: "asset_disposal" },
          { text: "Asset Checker", link: "asset_checker" },
          { text: "Close Period Asset", link: "close_period" },
        ],
      },
      {
        text: "Comment and Document Management & Activity Log",
        collapsed: true,
        base: '/carmen_cloud/comment/CM-',
        items: [
          { text: "Comment and Document Management & Activity Log", link: "comment" },
        ],
      },
     
      {
        text: "Work Book",
        collapsed: true,
        items: [
          { text: "Installation and Configuration", link: "/workbook/install&config" },
          { text: "Work Book Function", link: "/workbook/function" },
        ],
      },
      {
        text: "Configuration",
        collapsed: true,
        items: [
          { text: "Product License", link: "/configuration/product_license" },
          { text: "Company Profile", link: "/configuration/company_profile" },
          { text: "System Preference", link: "/configuration/system_preference" },
          { text: "Users", link: "/configuration/users" },
          { text: "Change Password User", link: "/configuration/change_password_user" },
          { text: "Permissions", link: "/configuration/permissions" },
          { text: "Currency Exchange Rate", link: "/configuration/currency_exrate" },
          { text: "Currency", link: "/configuration/currency" },
          { text: "Department", link: "/configuration/department" },
          { text: "Chart Of Accounts", link: "/configuration/chart_of_account" },
          { text: "Payment Type", link: "/configuration/payment_type" },
          { text: "Dimension", link: "/configuration/dimension" },
          { text: "Unit", link: "/configuration/unit" },
        ],
      },
    ]
  }
 

function sidebarTraining() {
  return [
    {
      text: "Carmen Cloud",
      collapsed: false,
      items: [
        {
          text: "Account Payable",
          collapsed: true,
          items: [
            {
              text: "Vendor_Profile",
              link: "/carmen_cloud/AP/index",
            },
            {
              text: "Invoice",
              link: "/carmen_cloud/AP/index1",
            },
            {
              text: "Payment",
              link: "/carmen_cloud/AP/index2",
            },
            {
              text: "Input_Vat_Reconciliation",
              link: "/carmen_cloud/AP/index3",
            },
            {
              text: "Withholding_Tax_Reconciliation",
              link: "/carmen_cloud/AP/index4",
            },
            
          ],
        },
        {
          text: "Account Receivable",
          collapsed: true,
          items: [
            {
              text: "Customer(AR)Profile",
              link: "/carmen_cloud/AR/index1",
            },
            {
              text: "Invoice",
              link: "/carmen_cloud/AR/index2",
            },
            {
              text: "Create Invoice from City Ledger Folio",
              link: "/carmen_cloud/AR/index3",
            },
            {
              text: "Receipt",
              link: "/carmen_cloud/AR/index4",
            },
          ],
        },
        {
          text: "Fixed Asset",
          collapsed: true,
          items: [
            {
              text: "Asset Registration",
              link: "/carmen_cloud/Fixed Asset/index1",
            },
            {
              text: "Batch Asset Registration",
              link: "/carmen_cloud/Fixed Asset/index2",
            },
            {
              text: "Disposal Asset",
              link: "/carmen_cloud/Fixed Asset/index3",
            },
          ],
        },
        {
          text: "Asset Checker",
          collapsed: true,
          items: [
            {
              text: "Mobile Asset Checking ",
              link: "/carmen_cloud/Asset Checker/index1",
            },
          ],
        },
        {
          text: "General Ledger",
          collapsed: true,
          items: [
            {
              text: "Journal Voucher",
              link: "/carmen_cloud/General_Ledger/index",
            },
            {
              text: "Copy Function on JV",
              link: "/carmen_cloud/General_Ledger/index1",
            },
            {
              text: "Create and Apply Template Voucher",
              link: "/carmen_cloud/General_Ledger/index2",
            },
            {
              text: "Allocation Voucher ",
              link: "/carmen_cloud/General_Ledger/index3",
            },
            {
              text: "Recurring Voucher",
              link: "/carmen_cloud/General_Ledger/index4",
            },
            {
              text: "Amortization Voucher",
              link: "/carmen_cloud/General_Ledger/index5",
            },
            {
              text: "Budget",
              link: "/carmen_cloud/General_Ledger/index6",
            },
            {
              text: "Posting from Other Modules",
              link: "/carmen_cloud/General_Ledger/index7",
            },
            {
              text: "Year Ending",
              link: "/carmen_cloud/General_Ledger/index8",
            },
          ],
        },
        {
          text: "Work Book",
          collapsed: true,
          items: [
            {
              text: "set up a business unit (BU)",
              link: "/carmen_cloud/Work_Book/index1",
            },

            {
              text: "How to upload a journal voucher (JV) from excel",
              link: "/carmen_cloud/Work_Book/index2",
            },

            {
              text: "How to upload JV allocation from excel",
              link: "/carmen_cloud/Work_Book/index3",
            },

            {
              text: "How to upload a budget from excel",
              link: "/carmen_cloud/Work_Book/index4",
            },
          ],
        },
      ],
    },
    {
      text: "Carmen On-Permise",
      collapsed: false,
      items: [
        {
          text: "Inventory",
          collapsed: true,
          items: [
            {
              text: "Receiving",
              link: "/carmen_onpermise/Receiving/index1",
            },

            {
              text: "Requisition",
              link: "/carmen_onpermise/Receiving/index2",
            },

            {
              text: "Transfer",
              link: "/carmen_onpermise/Receiving/index3",
            },

            {
              text: "Issue",
              link: "/carmen_onpermise/Receiving/index4",
            },

            {
              text: "Adjustmen/Sale",
              link: "/carmen_onpermise/Receiving/index5",
            },

            {
              text: "Procedure",
              link: "/carmen_onpermise/Receiving/index6",
            },

            {
              text: "Report",
              link: "/carmen_onpermise/Receiving/index7",
            },
          ],
        },
        {
          text: "Recipe",
          collapsed: true,
          items: [
            {
              text: "Recipe",
              link: "/carmen_onpermise/Receiving/index8",
            },
          ],
        },
        {
          text: "Asset Management",
          collapsed: true,
          items: [
            {
              text: "Asset Register",
              link: "/carmen_onpermise/Asset_Register/index1",
            },

            {
              text: "Procedure",
              link: "/carmen_onpermise/Asset_Procedure/index1",
            },

            {
              text: "Asset Disposal",
              link: "/carmen_onpermise/Asset_Disposal/index1",
            },

            {
              text: "Report",
              link: "/carmen_onpermise/Asset_Report/index1",
            },
          ],
        },
        {
          text: "General Ledger",
          collapsed: true,
          items: [
            {
              text: "Chart of Account",
              link: "/carmen_onpermise/GL_ChartofAccount/index1",
            },

            {
              text: "Budget",
              link: "/carmen_onpermise/GL_Budget/index1",
            },

            {
              text: "Journal Voucher",
              link: "/carmen_onpermise/GL_Journal_Voucher/index1",
            },

            {
              text: "Standard Voucher (Recurring) and Data Posting",
              link: "/carmen_onpermise/GL_Recurring/index1",
            },

            {
              text: "Close Period and Year End",
              link: "/carmen_onpermise/ClosePeriod_and_Year_End/index1",
            },

            {
              text: "Report",
              link: "/carmen_onpermise/GL_Report/index1",
            },
          ],
        },
        {
          text: "Add In",
          collapsed: true,
          items: [
            {
              text: "Financial Report",
              link: "/carmen_onpermise/Addin_FinancialReport/index1",
            },
          ],
        },
        {
          text: "Account Payable",
          collapsed: true,
          items: [
            {
              text: "Cloud Highlight",
              link: "/carmen_onpermise/AP_Cloud_Highlight/index1",
            },

            {
              text: "Vendor",
              link: "/carmen_onpermise/AP_Vendor/index1",
            },

            {
              text: "Invoice",
              link: "/carmen_onpermise/AP_Invoice/index1",
            },

            {
              text: "Payment",
              link: "/carmen_onpermise/AP_Payment/index1",
            },

            {
              text: "Procedure",
              link: "/carmen_onpermise/AP_Procedure/index1",
            },

            {
              text: "Report",
              link: "/carmen_onpermise/AP_Report/index1",
            },
          ],
        },
        {
          text: "Account Receivable",
          collapsed: true,
          items: [
            {
              text: "AR Profile",
              link: "/carmen_onpermise/AR_Profile/index1",
            },

            {
              text: "Invoice",
              link: "/carmen_onpermise/AR_Invoice/index1",
            },

            {
              text: "Receipt",
              link: "/carmen_onpermise/AR_Receipt/index1",
            },

            {
              text: "Report",
              link: "/carmen_onpermise/AR_Report/index1",
            },
          ],
        },
      ],
    },
    {
      text: "Cadena",
      collapsed: false,
      items: [
        {
          text: "Time Attandance",
          collapsed: true,
          items: [
            {
              text: "TA Data Setup",
              link: "/carmen_onpermise/TA Data Setup/index1",
            },
            
            {
              text: "TA Holiday Data Setup",
              link: "/carmen_onpermise/TA Holiday Data Setup/index1",
            },
          ],
        },
        {
          text: "Staffing",
          collapsed: true,
          items: [
            {
              text: "Transaction",
              link: "/carmen_onpermise/Transaction/index1",
            },
            {
              text: "Staffing Data Setup",
              link: "/carmen_onpermise/Staffing Data Setup/index1",
            },
            {
              text: "Resignation",
              link: "/carmen_onpermise/Cadena_Resignation/index1",
            },
            {
              text: "Employee Profile",
              link: "/carmen_onpermise/Employee Profile/index1",
            },
            {
              text: "Add New Employee",
              link: "/carmen_onpermise/Add New Employee/index1",
            },
          ],
        },
        {
          text: "System Setting",
          collapsed: true,
          items: [
            {
              text: "Workflow Management",
              link: "/carmen_onpermise/Workflow Management/index1",
            },
            {
              text: "Security",
              link: "/carmen_onpermise/Security/index1",
            },
            {
              text: "Import",
              link: "/carmen_onpermise/Cadena_Import/index1",
            },
            {
              text: "General Settings",
              link: "/carmen_onpermise/General Settings/index1",
            },
            {
              text: "Email Management",
              link: "/carmen_onpermise/Email Management/index1",
            },
          ],
        },
        {
          text: "Leave Management",
          collapsed: true,
          items: [
            {
              text: "Leave Data Setup",
              link: "/carmen_onpermise/Leave Data Setup/index1",
            },
          
          ],
        },
      ],
    },
  ];
}
