from django.db import migrations

class Migration(migrations.Migration):
    pass
    # dependencies = [
    #     ('positions', '0001_position_ship'),
    # ]
    #
    # operations = [
    #      migrations.RunSQL("ALTER TABLE positions_position ADD CONSTRAINT fk_ship_imo FOREIGN KEY (imo) \
    #                        REFERENCES positions_ship (imo) ON DELETE CASCADE ON UPDATE NO ACTION;")
    # ]