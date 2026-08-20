from client import MultiPlatformCreatorAttributionAnalyticsClient

def main():
    client = MultiPlatformCreatorAttributionAnalyticsClient()
    res = client.analyze_attribution("camp_summer_global_2026")
    print(f"Attributed GMV: ${res['attributed_gmv_usd']}")
    print(f"Conversion Rate: {res['conversion_rate_pct']}%")
    print(f"Top Channel: {res['top_performing_channel']}")

if __name__ == "__main__":
    main()
