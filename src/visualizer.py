import os
import glob
import pandas as pd
import plotly.graph_objects as go
import streamlit as st

from util.helpers.beat_annotations import *
from util.helpers.file_checker import *
from util.helpers.downloader import *
from util.helpers.reader import *

def load_data(record_path, record_id):
    """
    Loads record data and annotations from the MIT-BIH Arrhythmia Database.

    Parameters:
        :param `record_path (str)`: Path to the data folder.
        :param `record_id (str)`: ID of the record to load.

    Returns:
        :return tuple: A tuple containing the record data and annotations.
        If loading fails, returns (None, None).
    """
    try:
        record, annotation = load_data_mit(record_path, record_id)
        return record, annotation
    except Exception as e:
        st.error(f"Failed to load record data: {e}")
        return None, None

def main():

    st.title('MIT-BIH Arrhythmia DB Visualizer')

    record_path = st.text_input('Enter the path to the directory where the files are located', './data/mit-bih-arrhythmia-database')

    # Get the list of record IDs
    list_records = [os.path.basename(file)[:-4] for file in glob.glob(f'{record_path}/*.dat')]

    if len(list_records) == 0:
        st.warning(f'Records were not found in the specified path: {record_path}, ' +
                   'please enter the correct path for the files.')
        st.stop()

    record_id = st.selectbox('Select a record:', list_records)

    record, annotation = load_data(record_path, record_id)

    if record is not None and annotation is not None:
        
        st.subheader('Signals in this record:')
        for idx, signal in enumerate(record.sig_name):
            st.write(f'+ `{signal}` : in {record.units[idx]}, with a frequency of {record.fs * record.samps_per_frame[idx]}hz')

        st.subheader('Comments present in the record:')
        if record.comments:
            for comment in record.comments:
                st.write(f'+ {comment}')
        else:
            st.write('+ No comments found.')

        signals_df = pd.DataFrame(record.p_signal, columns=record.sig_name) 
        annot_serie = pd.Series(annotation.symbol, index=annotation.sample, name='annotations')
        full_df = pd.concat([signals_df, annot_serie], axis=1)

        st.subheader('Annotations')
        beat_annot_count = annot_serie.isin(dict(beat_annotations)).sum()
        non_beat_annot_count = annot_serie.isin(dict(non_beat_annotations)).sum()
        unique_annot = annot_serie.value_counts().index.values
        st.write(f'This record contains `{annot_serie.size}` annotations with `{beat_annot_count}` beat annotations and `{non_beat_annot_count}` non beat annotation(s).')
        st.write('The annotations are the following:')
        for annot in unique_annot:
            st.write(f'+ `{annot}` : {annotations.get(annot, "Unknown")}')

        st.subheader('Statistics')
        annot_counts_df = annot_serie.value_counts().rename_axis('annotations').reset_index(name='counts')
        bar_fig = go.Figure(data=[go.Bar(x=annot_counts_df['annotations'],
                                         y=annot_counts_df['counts'],
                                         text=annot_counts_df['counts'],
                                         textposition='auto')])
        bar_fig.update_layout(title='Annotations by count', yaxis_title='counts', xaxis_title='annotations')
        st.plotly_chart(bar_fig)

        annot_counts_df['percentage'] = 100 * annot_counts_df['counts'] / annot_counts_df['counts'].sum()
        pie_fig = go.Figure(data=[go.Pie(labels=annot_counts_df['annotations'],
                                         values=annot_counts_df['percentage'],
                                         textinfo='label+percent',
                                         insidetextorientation='radial')])
        pie_fig.update_layout(title='Annotations by percentage')
        st.plotly_chart(pie_fig)

        # Plot signals and annotations
        signal = st.selectbox('Select signal type', record.sig_name)
        matching_rows_by_annot = {}

        for annot in unique_annot:
            matching_rows_by_annot[annot] = full_df['annotations'] == annot

        fig = go.Figure(layout=go.Layout(title=go.layout.Title(
            text='{} signal with annotations'.format(signal))))
        
        fig.add_trace(go.Scatter(x=full_df.index.values,
                                 y=full_df[signal],
                                 mode='lines',
                                 name=signal))
        
        for annot, annot_matching_rows in matching_rows_by_annot.items():
            fig.add_trace(go.Scatter(x=full_df.index[annot_matching_rows].values,
                                     y=full_df[annot_matching_rows][signal].values,
                                     mode='markers',
                                     name='{} (annot)'.format(annot)))
        st.plotly_chart(fig)

if __name__ == "__main__":
    main()