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
      items: [
        { text: "Journal Voucher", link: "/gl/journal_voucher" },
        { text: "Template Voucher", link: "/gl/template_voucher" },
        { text: "Recurring Voucher", link: "/gl/recurring_voucher" },
        { text: "Amortization Voucher", link: "/gl/amortization_voucher" },
        { text: "Allocation Voucher", link: "/gl/allocation_voucher" },
        { text: "Budget", link: "/gl/budget" },
        { text: "Posting Account Payable to GL", link: "/gl/posting_ap" },
        { text: "Posting Account Receivable to GL", link: "/gl/posting_ar" },
        { text: "Inventory & Extra Cost Posting to GL", link: "/gl/posting_inventory" },
        { text: "Posting Fixed Assets to GL", link: "/gl/posting_asset" },
        { text: "Close Period and Year End", link: "/gl/close_period" },
      ],
    },
    {
      text: "Account Payable",
      collapsed: true,
      items: [
        { text: "Vendor", link: "/ap/vendor" },
        { text: "Posting AP invoice from recieving", link: "/ap/recevingToAp" },
        { text: "Invoice", link: "/ap/invoice" },
        { text: "Payment", link: "/ap/payment" },
        { text: "Deposit Payment", link: "/ap/deposit_payment" },
        { text: "Apply Deposit with Invoice", link: "/ap/apply_deposit_pay_with_inv" },
        { text: "Cheque Reconciliation", link: "/ap/cheque_reconciliation" },
        { text: "Input Tax Reconciliation", link: "/ap/input_tax_reconciliation" },
        { text: "WHT Reconciliation", link: "/ap/wht_reconciliation" },
        { text: "RDPrep_การโอนย้ายข้อมูลใบแนบ ภงด 3", link: "/ap/RDPrep_3" },
        { text: "RDPrep_การโอนย้ายข้อมูลใบแนบ ภงด 53", link: "/ap/RDPrep_53" },
        { text: "Close Period AP", link: "/ap/close_period" },
      ],
    },
    {
      text: "Account Receivable",
      collapsed: true,
      items: [
        { text: "Profile", link: "/ar/profile" },
        { text: "AR Posting from PMS (PMS Interface)", link: "/ar/posting_pms" },
        { text: "Folio", link: "/ar/folio" },
        { text: "Invoice", link: "/ar/invoice" },
        { text: "Contract", link: "/ar/contract" },
        { text: "Apply AR Contract", link: "/ar/apply_contract" },
        { text: "Receipt", link: "/ar/receipt" },
        { text: "Receipt for Advance Deposit", link: "/ar/receipt_advance_deposit" },
        { text: "Apply invoice for Advance Deposit", link: "/ar/apply_invoice_advance_deposit" },
        { text: "Close Period AR", link: "/ar/close_period" },
      ],
    },
    {
      text: "Asset",
      collapsed: true,
      items: [
        { text: "Pre-Register Asset Setting", link: "/asset/preasset_setting" },
        { text: "Pre-Register Asset", link: "/asset/preasset" },
        { text: "Asset Register", link: "/asset/asset_register" },
        { text: "Print Asset QR Code", link: "/asset/print_asset" },
        { text: "Asset Disposal", link: "/asset/asset_disposal" },
        { text: "Asset Checker", link: "/asset/asset_checker" },
        { text: "Close Period Asset", link: "/asset/close_period" },
      ],
    },
    {
      text: "Comment and Document Management & Activity Log",
      link: "/comment/",
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
  ];
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
              text: "on-permise GL",
              link: "/carmen_onpermise/AR",
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
          text: "Account Payable",
          collapsed: true,
          items: [
            {
              text: "on-permise AP",
              link: "/carmen_onpermise/AP",
            },
          ],
        },
        {
          text: "AR",
          collapsed: true,
          items: [
            {
              text: "on-permise AR",
              link: "/carmen_onpermise/AR",
            },
          ],
        },
        {
          text: "GL",
          collapsed: true,
          items: [
            {
              text: "on-permise GL",
              link: "/carmen_onpermise/GL",
            },
          ],
        },
      ],
    },
    {
      text: "Cadena",
      collapsed: false,
      items: [],
    },
  ];
}
