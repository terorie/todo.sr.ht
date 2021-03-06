"""Add CASCADE to tracker deletions

Revision ID: cd94e721e6b0
Revises: 030c8f83a75d
Create Date: 2018-12-12 22:16:01.893712

"""

# revision identifiers, used by Alembic.
revision = 'cd94e721e6b0'
down_revision = '030c8f83a75d'

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.drop_constraint(
            constraint_name="event_ticket_id_fkey",
            table_name="event",
            type_="foreignkey")
    op.create_foreign_key(
            constraint_name="event_ticket_id_fkey",
            source_table="event",
            referent_table="ticket",
            local_cols=["ticket_id"],
            remote_cols=["id"],
            ondelete="CASCADE")
    op.drop_constraint(
            constraint_name="event_comment_id_fkey",
            table_name="event",
            type_="foreignkey")
    op.create_foreign_key(
            constraint_name="event_comment_id_fkey",
            source_table="event",
            referent_table="ticket_comment",
            local_cols=["comment_id"],
            remote_cols=["id"],
            ondelete="CASCADE")
    op.drop_constraint(
            constraint_name="event_label_id_fkey",
            table_name="event",
            type_="foreignkey")
    op.create_foreign_key(
            constraint_name="event_label_id_fkey",
            source_table="event",
            referent_table="label",
            local_cols=["label_id"],
            remote_cols=["id"],
            ondelete="CASCADE")
    op.drop_constraint(
            constraint_name="event_notification_event_id_fkey",
            table_name="event_notification",
            type_="foreignkey")
    op.create_foreign_key(
            constraint_name="event_notification_event_id_fkey",
            source_table="event_notification",
            referent_table="event",
            local_cols=["event_id"],
            remote_cols=["id"],
            ondelete="CASCADE")
    op.drop_constraint(
            constraint_name="label_tracker_id_fkey",
            table_name="label",
            type_="foreignkey")
    op.create_foreign_key(
            constraint_name="label_tracker_id_fkey",
            source_table="label",
            referent_table="tracker",
            local_cols=["tracker_id"],
            remote_cols=["id"],
            ondelete="CASCADE")
    op.drop_constraint(
            constraint_name="ticket_label_ticket_id_fkey",
            table_name="ticket_label",
            type_="foreignkey")
    op.create_foreign_key(
            constraint_name="ticket_label_ticket_id_fkey",
            source_table="ticket_label",
            referent_table="ticket",
            local_cols=["ticket_id"],
            remote_cols=["id"],
            ondelete="CASCADE")
    op.drop_constraint(
            constraint_name="ticket_label_label_id_fkey",
            table_name="ticket_label",
            type_="foreignkey")
    op.create_foreign_key(
            constraint_name="ticket_label_label_id_fkey",
            source_table="ticket_label",
            referent_table="label",
            local_cols=["label_id"],
            remote_cols=["id"],
            ondelete="CASCADE")
    op.drop_constraint(
            constraint_name="ticket_tracker_id_fkey",
            table_name="ticket",
            type_="foreignkey")
    op.create_foreign_key(
            constraint_name="ticket_tracker_id_fkey",
            source_table="ticket",
            referent_table="tracker",
            local_cols=["tracker_id"],
            remote_cols=["id"],
            ondelete="CASCADE")
    op.drop_constraint(
            constraint_name="ticket_dupe_of_id_fkey",
            table_name="ticket",
            type_="foreignkey")
    op.create_foreign_key(
            constraint_name="ticket_dupe_of_id_fkey",
            source_table="ticket",
            referent_table="ticket",
            local_cols=["dupe_of_id"],
            remote_cols=["id"],
            ondelete="SET NULL")
    op.drop_constraint(
            constraint_name="ticket_comment_ticket_id_fkey",
            table_name="ticket_comment",
            type_="foreignkey")
    op.create_foreign_key(
            constraint_name="ticket_comment_ticket_id_fkey",
            source_table="ticket_comment",
            referent_table="ticket",
            local_cols=["ticket_id"],
            remote_cols=["id"],
            ondelete="CASCADE")
    op.drop_constraint(
            constraint_name="ticket_subscription_tracker_id_fkey",
            table_name="ticket_subscription",
            type_="foreignkey")
    op.create_foreign_key(
            constraint_name="ticket_subscription_tracker_id_fkey",
            source_table="ticket_subscription",
            referent_table="tracker",
            local_cols=["tracker_id"],
            remote_cols=["id"],
            ondelete="CASCADE")
    op.drop_constraint(
            constraint_name="ticket_subscription_ticket_id_fkey",
            table_name="ticket_subscription",
            type_="foreignkey")
    op.create_foreign_key(
            constraint_name="ticket_subscription_ticket_id_fkey",
            source_table="ticket_subscription",
            referent_table="ticket",
            local_cols=["ticket_id"],
            remote_cols=["id"],
            ondelete="CASCADE")
    op.drop_constraint(
            constraint_name="ticket_seen_ticket_id_fkey",
            table_name="ticket_seen",
            type_="foreignkey")
    op.create_foreign_key(
            constraint_name="ticket_seen_ticket_id_fkey",
            source_table="ticket_seen",
            referent_table="ticket",
            local_cols=["ticket_id"],
            remote_cols=["id"],
            ondelete="CASCADE")
    op.drop_constraint(
            constraint_name="ticket_assignee_ticket_id_fkey",
            table_name="ticket_assignee",
            type_="foreignkey")
    op.create_foreign_key(
            constraint_name="ticket_assignee_ticket_id_fkey",
            source_table="ticket_assignee",
            referent_table="ticket",
            local_cols=["ticket_id"],
            remote_cols=["id"],
            ondelete="CASCADE")


def downgrade():
    op.drop_constraint(
            constraint_name="event_ticket_id_fkey",
            table_name="event",
            type_="foreignkey")
    op.create_foreign_key(
            constraint_name="event_ticket_id_fkey",
            source_table="event",
            referent_table="ticket",
            local_cols=["ticket_id"],
            remote_cols=["id"])
    op.drop_constraint(
            constraint_name="event_comment_id_fkey",
            table_name="event",
            type_="foreignkey")
    op.create_foreign_key(
            constraint_name="event_comment_id_fkey",
            source_table="event",
            referent_table="ticket_comment",
            local_cols=["comment_id"],
            remote_cols=["id"])
    op.drop_constraint(
            constraint_name="event_label_id_fkey",
            table_name="event",
            type_="foreignkey")
    op.create_foreign_key(
            constraint_name="event_label_id_fkey",
            source_table="event",
            referent_table="label",
            local_cols=["label_id"],
            remote_cols=["id"])
    op.drop_constraint(
            constraint_name="event_notification_event_id_fkey",
            table_name="event_notification",
            type_="foreignkey")
    op.create_foreign_key(
            constraint_name="event_notification_event_id_fkey",
            source_table="event_notification",
            referent_table="event",
            local_cols=["event_id"],
            remote_cols=["id"])
    op.drop_constraint(
            constraint_name="label_tracker_id_fkey",
            table_name="label",
            type_="foreignkey")
    op.create_foreign_key(
            constraint_name="label_tracker_id_fkey",
            source_table="label",
            referent_table="tracker",
            local_cols=["tracker_id"],
            remote_cols=["id"])
    op.drop_constraint(
            constraint_name="ticket_label_ticket_id_fkey",
            table_name="ticket_label",
            type_="foreignkey")
    op.create_foreign_key(
            constraint_name="ticket_label_ticket_id_fkey",
            source_table="ticket_label",
            referent_table="ticket",
            local_cols=["ticket_id"],
            remote_cols=["id"])
    op.drop_constraint(
            constraint_name="ticket_label_label_id_fkey",
            table_name="ticket_label",
            type_="foreignkey")
    op.create_foreign_key(
            constraint_name="ticket_label_label_id_fkey",
            source_table="ticket_label",
            referent_table="label",
            local_cols=["label_id"],
            remote_cols=["id"])
    op.drop_constraint(
            constraint_name="ticket_tracker_id_fkey",
            table_name="ticket",
            type_="foreignkey")
    op.create_foreign_key(
            constraint_name="ticket_tracker_id_fkey",
            source_table="ticket",
            referent_table="tracker",
            local_cols=["tracker_id"],
            remote_cols=["id"])
    op.drop_constraint(
            constraint_name="ticket_dupe_of_id_fkey",
            table_name="ticket",
            type_="foreignkey")
    op.create_foreign_key(
            constraint_name="ticket_dupe_of_id_fkey",
            source_table="ticket",
            referent_table="ticket",
            local_cols=["dupe_of_id"],
            remote_cols=["id"])
    op.drop_constraint(
            constraint_name="ticket_comment_ticket_id_fkey",
            table_name="ticket_comment",
            type_="foreignkey")
    op.create_foreign_key(
            constraint_name="ticket_comment_ticket_id_fkey",
            source_table="ticket_comment",
            referent_table="ticket",
            local_cols=["ticket_id"],
            remote_cols=["id"])
    op.drop_constraint(
            constraint_name="ticket_subscription_tracker_id_fkey",
            table_name="ticket_subscription",
            type_="foreignkey")
    op.create_foreign_key(
            constraint_name="ticket_subscription_tracker_id_fkey",
            source_table="ticket_subscription",
            referent_table="tracker",
            local_cols=["tracker_id"],
            remote_cols=["id"])
    op.drop_constraint(
            constraint_name="ticket_subscription_ticket_id_fkey",
            table_name="ticket_subscription",
            type_="foreignkey")
    op.create_foreign_key(
            constraint_name="ticket_subscription_ticket_id_fkey",
            source_table="ticket_subscription",
            referent_table="ticket",
            local_cols=["ticket_id"],
            remote_cols=["id"])
    op.drop_constraint(
            constraint_name="ticket_seen_ticket_id_fkey",
            table_name="ticket_seen",
            type_="foreignkey")
    op.create_foreign_key(
            constraint_name="ticket_seen_ticket_id_fkey",
            source_table="ticket_seen",
            referent_table="ticket",
            local_cols=["ticket_id"],
            remote_cols=["id"])
    op.drop_constraint(
            constraint_name="ticket_assignee_ticket_id_fkey",
            table_name="ticket_assignee",
            type_="foreignkey")
    op.create_foreign_key(
            constraint_name="ticket_assignee_ticket_id_fkey",
            source_table="ticket_assignee",
            referent_table="ticket",
            local_cols=["ticket_id"],
            remote_cols=["id"])
