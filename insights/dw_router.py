class DataWarehouseRouter:
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'snowflake':
            return 'dw'
        return None

    def allow_relation(self, o1, o2, **hints):
        if o1._meta.app_label == 'snowflake' or o2._meta.app_label == 'snowflake':
            return True
        return None
