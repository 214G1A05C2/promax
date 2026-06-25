import theme from "./theme";

const styles = {
  page: {
    padding: "20px",
    background: `linear-gradient(180deg, ${theme.colors.surface} 0%, ${theme.colors.pageBg} 100%)`,
    minHeight: "100vh",
    fontFamily: theme.typography.fontFamily,
    color: theme.colors.text,
  },

  shell: {
    width: "100%",
    maxWidth: "none",
    margin: "0 auto",
  },

  loading: {
    height: "100vh",
    display: "flex",
    justifyContent: "center",
    alignItems: "center",
    fontSize: "22px",
    fontWeight: 600,
    color: theme.colors.textMuted,
    background: theme.colors.pageBg,
  },

  errorBanner: {
    display: "flex",
    justifyContent: "space-between",
    alignItems: "center",
    gap: "16px",
    padding: "14px 16px",
    marginBottom: "20px",
    borderRadius: theme.radius.sm,
    background: "#FFF8F1",
    border: "1px solid #FED7AA",
    color: "#9A3412",
    boxShadow: theme.shadows.card,
  },

  errorTitle: {
    fontSize: "16px",
    fontWeight: "bold",
    marginBottom: "4px",
  },

  errorText: {
    fontSize: "14px",
    lineHeight: 1.4,
  },

  retryButton: {
    padding: "10px 14px",
    border: "none",
    borderRadius: theme.radius.sm,
    background: theme.colors.danger,
    color: "white",
    fontWeight: "bold",
    cursor: "pointer",
    whiteSpace: "nowrap",
    boxShadow: theme.shadows.soft,
  },

  header: {
    display: "flex",
    justifyContent: "space-between",
    alignItems: "center",
    gap: "20px",
    marginBottom: "18px",
    padding: "20px 22px",
    background: "rgba(255, 255, 255, 0.94)",
    border: `1px solid ${theme.colors.border}`,
    borderRadius: theme.radius.lg,
    boxShadow: theme.shadows.panel,
    backdropFilter: "blur(12px)",
    flexWrap: "wrap",
  },

  headerCopy: {
    display: "flex",
    flexDirection: "column",
    gap: "8px",
  },

  title: {
    margin: 0,
    fontSize: "34px",
    fontWeight: 700,
    letterSpacing: "-0.03em",
    lineHeight: 1.1,
  },

  filterContainer: {
    display: "flex",
    gap: "12px",
    flexWrap: "wrap",
    alignItems: "center",
    marginLeft: "auto",
  },

  select: {
    height: "44px",
    padding: "0 14px",
    borderRadius: theme.radius.sm,
    border: `1px solid ${theme.colors.border}`,
    background: theme.colors.surface,
    color: theme.colors.text,
    boxShadow: theme.shadows.inset,
    minWidth: "138px",
    fontSize: "14px",
  },

  button: {
    height: "44px",
    padding: "0 16px",
    background: theme.gradients.primary,
    color: "white",
    border: "none",
    borderRadius: theme.radius.sm,
    cursor: "pointer",
    boxShadow: theme.shadows.card,
    fontWeight: 700,
    fontSize: "14px",
  },

  chartGrid: {
    display: "grid",
    gridTemplateColumns: "1.15fr 0.85fr",
    gap: "18px",
    marginTop: "18px",
  },

  chartCard: {
    background: "rgba(255,255,255,0.98)",
    padding: "20px",
    borderRadius: theme.radius.lg,
    boxShadow: theme.shadows.card,
    border: `1px solid ${theme.colors.border}`,
    transition: "transform 160ms ease, box-shadow 160ms ease",
    height: "100%",
  },

  chartHeaderRow: {
    display: "flex",
    alignItems: "center",
    justifyContent: "space-between",
    gap: "16px",
    marginBottom: "18px",
  },

  chartHeaderPill: {
    padding: "9px 12px",
    borderRadius: "999px",
    border: `1px solid ${theme.colors.border}`,
    background: "#F8FAFD",
    color: theme.colors.textMuted,
    fontSize: "13px",
    fontWeight: 600,
    whiteSpace: "nowrap",
  },

  chartHeaderSpacer: {
    width: "124px",
    height: "1px",
    flexShrink: 0,
  },

  monthCard: {
    background: "rgba(255,255,255,0.98)",
    padding: "20px",
    borderRadius: theme.radius.lg,
    marginTop: "18px",
    boxShadow: theme.shadows.card,
    border: `1px solid ${theme.colors.border}`,
    transition: "transform 160ms ease, box-shadow 160ms ease",
  },

  chartTitle: {
    fontSize: "18px",
    fontWeight: 700,
    marginBottom: "14px",
    color: theme.colors.text,
  },

  footer: {
    textAlign: "center",
    marginTop: "18px",
    fontWeight: 600,
    color: theme.colors.textMuted,
    fontSize: "13px",
    paddingBottom: "8px",
  },
};

export default styles;
