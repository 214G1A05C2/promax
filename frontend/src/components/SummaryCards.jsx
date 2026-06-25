import React from "react";
import {
  PhoneCall,
  CalendarCheck2,
  Headphones,
  VolumeX,
} from "lucide-react";
import theme from "../theme";

function SummaryCards({
  totalCalls,
  appointments,
  frontDeskCalls,
  silentCalls,
}) {
  const cards = [
    {
      title: "Total Calls",
      value: totalCalls,
      accent: theme.gradients.primary,
      icon: PhoneCall,
      tint: theme.colors.primarySoft,
      iconTint: theme.colors.primary,
    },
    {
      title: "Appointments",
      value: appointments,
      accent: theme.gradients.success,
      icon: CalendarCheck2,
      tint: theme.colors.successSoft,
      iconTint: theme.colors.success,
    },
    {
      title: "Front Desk",
      value: frontDeskCalls,
      accent: theme.gradients.warning,
      icon: Headphones,
      tint: theme.colors.warningSoft,
      iconTint: theme.colors.warning,
    },
    {
      title: "Silent Calls",
      value: silentCalls,
      accent: theme.gradients.accent,
      icon: VolumeX,
      tint: theme.colors.accentSoft,
      iconTint: theme.colors.accent,
    },
  ];

  return (
    <div className="summary-grid">
      {cards.map(({ title, value, accent, icon: Icon, tint, iconTint }) => (
      <div
        key={title}
        className="summary-card"
        style={{
            background: `linear-gradient(180deg, ${tint}, ${theme.colors.surface} 72%)`,
            borderRadius: theme.radius.md,
            boxShadow: theme.shadows.soft,
            color: theme.colors.text,
            padding: "18px",
            border: `1px solid ${theme.colors.border}`,
            minHeight: "132px",
            display: "flex",
            flexDirection: "column",
            justifyContent: "space-between",
            position: "relative",
            overflow: "hidden",
          }}
        >
          <div
            style={{
              position: "absolute",
              inset: "0 auto auto 0",
              width: "100%",
              height: "4px",
              background: accent,
            }}
          />

          <div
            style={{
              display: "flex",
              alignItems: "flex-start",
              justifyContent: "space-between",
              gap: "12px",
              paddingTop: "8px",
            }}
          >
            <div>
              <h4
                style={{
                  margin: 0,
                  fontSize: "12px",
                  fontWeight: 800,
                  letterSpacing: "0.14em",
                  textTransform: "uppercase",
                  color: theme.colors.textMuted,
                }}
              >
                {title}
              </h4>
              <h2
                style={{
                  margin: "10px 0 0",
                  fontSize: "40px",
                  lineHeight: 1,
                  fontWeight: 700,
                  letterSpacing: "-0.05em",
                  color: theme.colors.text,
                }}
              >
                {value}
              </h2>
            </div>

            <div
              style={{
                width: "58px",
                height: "58px",
                borderRadius: "18px",
                display: "grid",
                placeItems: "center",
                background: accent,
                border: "1px solid rgba(255,255,255,0.72)",
                boxShadow: "0 16px 34px rgba(37, 99, 235, 0.18)",
                flexShrink: 0,
              }}
            >
              <Icon size={26} color="#FFFFFF" strokeWidth={2.4} />
            </div>
          </div>
        </div>
      ))}
    </div>
  );
}

export default SummaryCards;
