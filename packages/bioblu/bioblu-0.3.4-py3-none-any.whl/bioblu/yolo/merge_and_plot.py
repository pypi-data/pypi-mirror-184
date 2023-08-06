#!/usr/bin/env python3

import copy
import logging
from dataclasses import dataclass
from matplotlib import pyplot as plt
import os
import pandas as pd
from typing import TypedDict, List

from bioblu.ds_manage import ds_annotations

logging.basicConfig(level=logging.INFO, format="%(levelname)s\t%(message)s")
logging.disable()

def to_alphanum(txt_in: str) -> str:
    return "".join([x for x in txt_in if x.isalnum()])


@dataclass
class MetaClass:
    name: str
    components: List[str]


def add_metaclasses(df_in: pd.DataFrame, metaclass_info: List[MetaClass]) -> pd.DataFrame:
    work_df = copy.deepcopy(df_in)
    for metaclass in metaclass_info:
        work_df.loc[work_df["Class"].isin(metaclass.components), "Metaclass"] = metaclass.name
        logging.info(metaclass.name)
    return work_df


fpath_class_results = "/media/findux/DATA/Documents/Malta_II/MDPI_paper/test_set_results_9571_ds17.csv"
graphics_savedir = "/media/findux/DATA/Documents/Malta_II/MDPI_paper/graphics/"
ds_root = "/media/findux/DATA/Documents/Malta_II/datasets/dataset_17_yolo/"


merging_info = [
    MetaClass(name="Plastic",
              components=["Other plastic", "Plastic bottle",  "Plastic bag",  "Plastic bottlecap", "Wrapper & foil",
                          "Plastic container", "Plastic clothes pin", "Plastic cup", "Straws", "Plastic floater", "Plastic wrapper & foil",
                          "Plastic utensils", "Tooth brush", "Styrofoam", "Plastic lid", "Garbage bag", "Lighter",
                          ]),
    MetaClass(name="Paper & Cardboard",
              components=["Paper cup", "Paper", "Paper bag",  "Tissue", "Cardboard", "Cigarette package", "Drink carton", "Egg carton"
                          ]),
    MetaClass(name="Glass",
              components=["Glass bottle", "Glass cup", "Glass jar", "Broken glass",
                          ]),
    MetaClass(name="Metal litter",
              components=["Aluminium foil", "Metal bottlecap", "Pop tab", "Metal can", "Metal", "Metal lid",
                          "Metal screw cap", "Scrap metal", "Hair pin",
                          ]),
    MetaClass(name="Clothing & Fabric",
              components=[
                  "Cloth", "Shoe", "Backpack",
              ]),
    MetaClass(name="Other",
              components=[
                  "Rope & string", "Battery", "Chair", "Cigarette butt", "Cigarette", "Cork stopper", "Diaper", "Dog",
                  "Facemask", "Lightbulb", "Match", "Grating", "Metal pole", "Person", "Pipe", "Plant pot", "QTip",
                  "Food waste", "Metal grating, fence", "Soccer ball", "Spark plug", "Squeezetube", "Table",
                  "Tennis ball", "Tile", "Tyre", "Wood", "Button",
              ])
    ]

class_metrics = ds_annotations.get_classes_summary(ds_root).reset_index()
class_metrics.to_csv("/home/findux/Desktop/class_metrics.csv")

assert os.path.exists(fpath_class_results)
results = pd.read_csv(fpath_class_results)

df_joined = class_metrics.merge(results, on="Class", how="outer")
df_joined.to_csv("/home/findux/Desktop/df_joined.csv")
logging.info(df_joined.columns)

df_joined_metaclasses = add_metaclasses(df_joined, merging_info)
df_joined_metaclasses.to_csv("/home/findux/Desktop/df_joined_metaclasses.csv")
logging.info(df_joined_metaclasses["Metaclass"].unique())

df_joined_metaclasses.loc[df_joined_metaclasses["Total_images"] < 10, "Metaclass"] = "N img < 10"

logging.info(df_joined_metaclasses["Metaclass"].unique())

df_joined_metaclasses.to_csv("/media/findux/DATA/Documents/Malta_II/MDPI_paper/joined_dataframe.csv")

# Add linebreaks
for src, dst in [
    ("Paper & Cardboard", "Paper &\nCardboard"),
    ("Clothing & Fabric", "Clothing &\nFabric"),
    ("N img <10", "N img\n>10"),
]:
    df_joined_metaclasses.loc[df_joined_metaclasses["Metaclass"] == src, "Metaclass"] = dst

name_replacements = [
    ("Plastic wrapper & foil", "Plastic wrapper\n& foil"),
    ("Metal grating, fence", "Grating"),
    ("Plastic clothes pin", "Clothes pin"),
]

for old_class, new_class in name_replacements:
    df_joined_metaclasses["Class"].replace(old_class, new_class, inplace=True)

df_joined_metaclasses.sort_values(by="Class").to_csv("/media/findux/DATA/Documents/Malta_II/MDPI_paper/joined_dataframe.csv")

col = "#005c46"
dpi = 600
pic_ext = "png"
subplotsbottom = 0.30

# Plotting class counts
df_sums = df_joined_metaclasses.groupby(by="Metaclass").sum().reset_index()
df_sums.sort_values(by="Metaclass", inplace=True)
fig_classes, ax = plt.subplots(1, 1)
plt.title("Number of instances per metaclass", fontweight='bold')
ax.grid(axis="y")
ax.set_axisbelow(True)
ax.bar(x=df_sums["Metaclass"], height=df_sums["Annotations"], color=col)
plt.ylabel("Number of instances", fontweight='bold')
plt.xlabel("Metaclass", fontweight='bold')
plt.subplots_adjust(bottom=0.15)
# Plot images per category
fig_imgs, ax = plt.subplots(1, 1)
plt.title("Number of images per class", fontweight='bold')
ax.grid(axis="y")
ax.set_axisbelow(True)
ax.bar(x=df_sums["Metaclass"], height=df_sums["Total_images"], color=col)
plt.ylabel("Number of images", fontweight='bold')
plt.xlabel("Metaclass", fontweight='bold')
plt.subplots_adjust(bottom=0.15)
# Plot avg class performance
df_avg = df_joined_metaclasses.groupby(by="Metaclass").mean().reset_index()
fig_perf, ax = plt.subplots(1, 1)
plt.title("mAP50-90 per Metaclass", fontweight='bold')
ax.grid(axis="y")
ax.set_axisbelow(True)
plt.ylim((0, 1))
ax.bar(x=df_avg["Metaclass"], height=df_avg["mAP50-95"], color=col)
plt.ylabel("mAP50-95", fontweight='bold')
plt.xlabel("Metaclass", fontweight='bold')
plt.subplots_adjust(bottom=0.15)

# Save plots
fig_classes.savefig(os.path.join(graphics_savedir, f"instance_metaclass_counts.{pic_ext}"), dpi=dpi)
fig_imgs.savefig(os.path.join(graphics_savedir, f"img_counts_per_class.{pic_ext}"), dpi=dpi)
fig_perf.savefig(os.path.join(graphics_savedir, f"map50-95_per_metaclass.{pic_ext}"), dpi=dpi)

# Plot per material:
logging.info(df_joined_metaclasses["Metaclass"].unique())
fig_results, axs = plt.subplots(1, 2)
plt.subplots_adjust(wspace=1.2)

df_cloth = df_joined_metaclasses[df_joined_metaclasses["Metaclass"] == "Clothing &\nFabric"].dropna()
plt.subplots_adjust(bottom=subplotsbottom)
axs[0].grid(axis="y")
axs[0].set_axisbelow(True)
axs[0].bar(x=df_cloth["Class"], height=df_cloth["mAP50-95"], color=col)
axs[0].set_ylim((0, 1))
axs[0].set_ylabel("mAP50-95", fontweight='bold')
axs[0].set_xlabel("Class", fontweight='bold')
axs[0].tick_params('x', labelrotation=90)
axs[0].set_title("Clothing & fabric", fontweight='bold')

df_glass = df_joined_metaclasses[df_joined_metaclasses["Metaclass"] == "Glass"].dropna()
axs[1].grid(axis="y")
axs[1].set_axisbelow(True)
axs[1].bar(x=df_glass["Class"], height=df_glass["mAP50-95"], color=col)
axs[1].set_ylim((0, 1))
axs[1].tick_params('x', labelrotation=90)
axs[1].set_ylabel("mAP50-95", fontweight='bold')
axs[1].set_xlabel("Class", fontweight='bold')
axs[1].set_title("Glass", fontweight='bold')
plt.subplots_adjust(bottom=subplotsbottom)
fig_results.savefig(os.path.join(graphics_savedir, f"doubleplot.{pic_ext}"), dpi=dpi)
plt.close()

for metaclass in df_joined_metaclasses["Metaclass"].unique():
    class_name = metaclass
    df_use = df_joined_metaclasses[df_joined_metaclasses["Metaclass"] == metaclass].dropna()
    fig_results, ax = plt.subplots(1, 1)
    ax.grid(axis="y")
    ax.set_axisbelow(True)
    ax.bar(x=df_use["Class"], height=df_use["mAP50-95"], color=col)
    plt.ylim((0, 1))
    plt.ylabel("mAP50-95", fontweight='bold')
    plt.xlabel("Class", fontweight='bold')
    plt.title(metaclass.replace("\n", " "), fontweight='bold')
    plt.xticks(rotation=90)
    plt.subplots_adjust(bottom=subplotsbottom)
    fig_results.savefig(os.path.join(graphics_savedir, f"performance_{to_alphanum(metaclass)}.{pic_ext}"), dpi=dpi)
    plt.close()

    fig_instance_counts, ax = plt.subplots(1, 1)
    ax.grid(axis="y")
    ax.set_axisbelow(True)
    ax.bar(x=df_use["Class"], height=df_use["Annotations"], color=col)
    plt.ylabel("Instance count", fontweight='bold')
    plt.xlabel("Class", fontweight='bold')
    plt.title(metaclass.replace("\n", " "), fontweight='bold')
    plt.xticks(rotation=90)
    plt.ylim(0, df_joined_metaclasses["Annotations"].max())
    plt.subplots_adjust(bottom=subplotsbottom)
    fig_instance_counts.savefig(os.path.join(graphics_savedir, f"instance_count_{to_alphanum(metaclass)}.{pic_ext}"), dpi=dpi)
    plt.close()


# Performance by img count
fig, ax = plt.subplots(1, 1)
x, y = df_joined_metaclasses["Total_images"], df_joined_metaclasses["mAP50-95"]
annots = list(df_joined_metaclasses["Class"])
ax.scatter(x, y)
plt.ylabel("mAP50-90")
plt.xlabel("Number of images per class")
plt.title("Class performance against class size (images)")
for i, cl in enumerate(annots):
    ax.annotate(cl, (x[i], y[i]))
fig.savefig(os.path.join(graphics_savedir, f"Perf_against_imgs.{pic_ext}"), dpi=dpi)


# Performance by annotation count
fig, ax = plt.subplots(1, 1)
x, y = df_joined_metaclasses["Annotations"], df_joined_metaclasses["mAP50-95"]
annots = list(df_joined_metaclasses["Class"])
ax.scatter(x, y)
plt.ylabel("mAP50-90")
plt.xlabel("Number of annotations per class")
plt.title("Class performance against class size (annotations)")
for i, cl in enumerate(annots):
    ax.annotate(cl, (x[i], y[i]))
fig.savefig(os.path.join(graphics_savedir, f"Perf_against_instances.{pic_ext}"), dpi=dpi)