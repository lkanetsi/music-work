
import pandas as pd
from django.core.management import BaseCommand
from django.utils import timezone

from app.models import MusicalWork


class Command(BaseCommand):
    help = "Loads musicalworks sheet from CSV file; cleans duplicates and missing fields."

    def add_arguments(self, parser):
        parser.add_argument("file_path", type=str)

    def handle(self, *args, **options):
        # start time for benchmarking and performance
        start_time = timezone.now()

        file_path = options["file_path"]
        data = pd.read_csv(file_path)
        # cleaning data 
        data = data.dropna(axis=0)

        # removing duplicates
        data.drop_duplicates(subset=None, keep='first', inplace=False)
        # lets index with row 
        data.reset_index()
        print(data)        
        # intialize list
        musicalwork = []

        for index,row in data.iterrows():
            musicalworks = MusicalWork(
                title=row[0],
                contributors=row[1],
                iswc=row[2],
            )
            musicalwork.append(musicalworks)
        # commint and save to the database
        if musicalwork:
            MusicalWork.objects.bulk_create(musicalwork)
        # for performance
        end_time = timezone.now()

        self.stdout.write(
            self.style.SUCCESS(
                f"Loading CSV took: {(end_time-start_time).total_seconds()} seconds."
            )
        )
