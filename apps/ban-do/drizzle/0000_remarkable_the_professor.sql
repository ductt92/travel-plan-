CREATE TYPE "public"."province_status" AS ENUM('none', 'visited', 'wish');--> statement-breakpoint
CREATE TABLE "provinces" (
	"code" text PRIMARY KEY NOT NULL,
	"status" "province_status" DEFAULT 'none' NOT NULL,
	"updated_at" timestamp with time zone DEFAULT now() NOT NULL
);
--> statement-breakpoint
CREATE TABLE "trips" (
	"id" serial PRIMARY KEY NOT NULL,
	"province_code" text NOT NULL,
	"from_date" date,
	"to_date" date,
	"companions" text DEFAULT '' NOT NULL,
	"rate" integer DEFAULT 0 NOT NULL,
	"places" jsonb DEFAULT '[]'::jsonb NOT NULL,
	"note" text DEFAULT '' NOT NULL,
	"created_at" timestamp with time zone DEFAULT now() NOT NULL,
	"updated_at" timestamp with time zone DEFAULT now() NOT NULL
);
--> statement-breakpoint
ALTER TABLE "trips" ADD CONSTRAINT "trips_province_code_provinces_code_fk" FOREIGN KEY ("province_code") REFERENCES "public"."provinces"("code") ON DELETE cascade ON UPDATE no action;--> statement-breakpoint
CREATE INDEX "trips_province_idx" ON "trips" USING btree ("province_code");--> statement-breakpoint
CREATE INDEX "trips_from_idx" ON "trips" USING btree ("from_date");