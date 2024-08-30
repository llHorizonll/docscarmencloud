import { defineConfig } from "vitepress";

// https://vitepress.dev/reference/site-config
export default defineConfig({
  title: "Carmen Cloud Manual",
  description: "Document for carmen.blue",
  themeConfig: {
    // https://vitepress.dev/reference/default-theme-config
    nav: [
      { text: "Home", link: "/" },
      {
        text: "Changelog",
        items: [
          {
            text: "🆕 July2024 Relaese Infomation",
            link: "/july2024",
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
            activeMatch:"/changelog/"
          },
        ],
      },
      // { text: "Examples", link: "/markdown-examples" },
    ],

    sidebar: [
      {
        text: "Dashboard",
        link: "/dashboard/",
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
    ],

    socialLinks: [{ icon: "github", link: "https://github.com/vuejs/vitepress" }],
    search: {
      provider: "local",
    },
  },
});
