from django.db import models

class ForecastDay(models.Model):
    postal_code = models.CharField(max_length=20, blank=True, null=True)
    country = models.CharField(max_length=2, blank=True, null=True)
    time_init_utc = models.DateField(blank=True, null=True)
    date_valid_std = models.DateField(blank=True, null=True)
    doy_std = models.BigIntegerField(blank=True, null=True)
    min_temperature_air_2m_f = models.DecimalField(max_digits=5, decimal_places=1, blank=True, null=True)
    avg_temperature_air_2m_f = models.DecimalField(max_digits=5, decimal_places=1, blank=True, null=True)
    max_temperature_air_2m_f = models.DecimalField(max_digits=5, decimal_places=1, blank=True, null=True)
    min_temperature_wetbulb_2m_f = models.DecimalField(max_digits=5, decimal_places=1, blank=True, null=True)
    avg_temperature_wetbulb_2m_f = models.DecimalField(max_digits=5, decimal_places=1, blank=True, null=True)
    max_temperature_wetbulb_2m_f = models.DecimalField(max_digits=5, decimal_places=1, blank=True, null=True)
    min_temperature_dewpoint_2m_f = models.DecimalField(max_digits=5, decimal_places=1, blank=True, null=True)
    avg_temperature_dewpoint_2m_f = models.DecimalField(max_digits=5, decimal_places=1, blank=True, null=True)
    max_temperature_dewpoint_2m_f = models.DecimalField(max_digits=5, decimal_places=1, blank=True, null=True)
    min_temperature_feelslike_2m_f = models.DecimalField(max_digits=5, decimal_places=1, blank=True, null=True)
    avg_temperature_feelslike_2m_f = models.DecimalField(max_digits=5, decimal_places=1, blank=True, null=True)
    max_temperature_feelslike_2m_f = models.DecimalField(max_digits=5, decimal_places=1, blank=True, null=True)
    min_temperature_windchill_2m_f = models.DecimalField(max_digits=5, decimal_places=1, blank=True, null=True)
    avg_temperature_windchill_2m_f = models.DecimalField(max_digits=5, decimal_places=1, blank=True, null=True)
    max_temperature_windchill_2m_f = models.DecimalField(max_digits=5, decimal_places=1, blank=True, null=True)
    min_temperature_heatindex_2m_f = models.DecimalField(max_digits=5, decimal_places=1, blank=True, null=True)
    avg_temperature_heatindex_2m_f = models.DecimalField(max_digits=5, decimal_places=1, blank=True, null=True)
    max_temperature_heatindex_2m_f = models.DecimalField(max_digits=5, decimal_places=1, blank=True, null=True)
    min_humidity_relative_2m_pct = models.BigIntegerField(blank=True, null=True)
    avg_humidity_relative_2m_pct = models.BigIntegerField(blank=True, null=True)
    max_humidity_relative_2m_pct = models.BigIntegerField(blank=True, null=True)
    min_humidity_specific_2m_gpkg = models.DecimalField(max_digits=5, decimal_places=1, blank=True, null=True)
    avg_humidity_specific_2m_gpkg = models.DecimalField(max_digits=5, decimal_places=1, blank=True, null=True)
    max_humidity_specific_2m_gpkg = models.DecimalField(max_digits=5, decimal_places=1, blank=True, null=True)
    min_pressure_2m_mb = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    avg_pressure_2m_mb = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    max_pressure_2m_mb = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    min_pressure_mean_sea_level_mb = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    avg_pressure_mean_sea_level_mb = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    max_pressure_mean_sea_level_mb = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    min_wind_speed_10m_mph = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True)
    avg_wind_speed_10m_mph = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True)
    max_wind_speed_10m_mph = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True)
    avg_wind_direction_10m_deg = models.BigIntegerField(blank=True, null=True)
    min_wind_speed_80m_mph = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True)
    avg_wind_speed_80m_mph = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True)
    max_wind_speed_80m_mph = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True)
    avg_wind_direction_80m_deg = models.BigIntegerField(blank=True, null=True)
    min_wind_speed_100m_mph = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True)
    avg_wind_speed_100m_mph = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True)
    max_wind_speed_100m_mph = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True)
    avg_wind_direction_100m_deg = models.BigIntegerField(blank=True, null=True)
    tot_precipitation_in = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    tot_snowfall_in = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    min_cloud_cover_tot_pct = models.BigIntegerField(blank=True, null=True)
    avg_cloud_cover_tot_pct = models.BigIntegerField(blank=True, null=True)
    max_cloud_cover_tot_pct = models.BigIntegerField(blank=True, null=True)
    min_radiation_solar_total_wpm2 = models.DecimalField(max_digits=5, decimal_places=1, blank=True, null=True)
    avg_radiation_solar_total_wpm2 = models.DecimalField(max_digits=5, decimal_places=1, blank=True, null=True)
    max_radiation_solar_total_wpm2 = models.DecimalField(max_digits=6, decimal_places=1, blank=True, null=True)
    tot_radiation_solar_total_wpm2 = models.DecimalField(max_digits=7, decimal_places=1, blank=True, null=True)
    probability_of_precipitation_pct = models.BigIntegerField(blank=True, null=True)
    probability_of_snow_pct = models.BigIntegerField(blank=True, null=True)


    class Meta:
        app_label = 'insights'
        managed = False
        db_table = 'FORECAST_DAY'
