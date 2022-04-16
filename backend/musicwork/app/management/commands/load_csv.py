
import pandas as pd
from django.core.management import BaseCommand
from django.utils import timezone

from app.models import MusicalWork


class Command(BaseCommand):
    help = "Loads musicalworks sheet from CSV file; cleans duplicates , missing data and combines data ."

    def add_arguments(self, parser):
        parser.add_argument("file_path", type=str)

    def convertor(self, contributors):
        """converts series data from pandas dataframe
        to the list for contributors column"""
        # type cast series to a list
        contributors = contributors.tolist()
        #remove duplicates using set
        contributors = set(contributors)
        # concant string
        contributors = ' | '.join(contributors)
        return contributors

    def handle(self, *args, **options):
        # start time for benchmarking and performance
        start_time = timezone.now()
        file_path = options["file_path"]
        #import CSV file 
        data = pd.read_csv(file_path)

        # cleaning data / dropping missing row  data NAN
        data = data.dropna(axis=0)
    
        # merge and consolidate duplicated data
        data = data.groupby('title').agg({
            'contributors':[self.convertor],
            'iswc': 'first'}).reset_index()
        print(data.describe)
        # intialize list to commit to the database
        musicalwork = []

        for index, row in data.iterrows():
            musicalworks = MusicalWork(
                title=row[0],
                contributors=row[1],
                iswc=row[2],
            )
            musicalwork.append(musicalworks)

        # commint and save to the database
        if musicalwork:
            MusicalWork.objects.bulk_create(musicalwork)

        end_time = timezone.now()

        self.stdout.write(
            self.style.SUCCESS(
                f"Loading CSV took: {(end_time-start_time).total_seconds()} seconds."
            )
        )
