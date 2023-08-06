import pandas as pd
import pytest

import causalpy as cp

sample_kwargs = {"tune": 20, "draws": 20, "chains": 2, "cores": 2}


@pytest.mark.integration
def test_did():
    df = cp.load_data("did")
    result = cp.pymc_experiments.DifferenceInDifferences(
        df,
        formula="y ~ 1 + group*post_treatment",
        time_variable_name="t",
        group_variable_name="group",
        model=cp.pymc_models.LinearRegression(sample_kwargs=sample_kwargs),
    )
    assert isinstance(df, pd.DataFrame)
    assert isinstance(result, cp.pymc_experiments.DifferenceInDifferences)
    assert len(result.idata.posterior.coords["chain"]) == sample_kwargs["chains"]
    assert len(result.idata.posterior.coords["draw"]) == sample_kwargs["draws"]


# TODO: set up fixture for the banks dataset


@pytest.mark.integration
def test_did_banks_simple():
    treatment_time = 1930.5
    df = (
        cp.load_data("banks")
        .filter(items=["bib6", "bib8", "year"])
        .rename(columns={"bib6": "Sixth District", "bib8": "Eighth District"})
        .groupby("year")
        .median()
    )
    # SET TREATMENT TIME TO ZERO =========
    df.index = df.index - treatment_time
    treatment_time = 0
    # ====================================
    df.reset_index(level=0, inplace=True)
    df_long = pd.melt(
        df,
        id_vars=["year"],
        value_vars=["Sixth District", "Eighth District"],
        var_name="district",
        value_name="bib",
    ).sort_values("year")
    df_long["unit"] = df_long["district"]
    df_long["post_treatment"] = df_long.year >= treatment_time
    df_long = df_long.replace({"district": {"Sixth District": 1, "Eighth District": 0}})

    result = cp.pymc_experiments.DifferenceInDifferences(
        # df_long[df_long.year.isin([1930, 1931])],
        df_long[df_long.year.isin([-0.5, 0.5])],
        formula="bib ~ 1 + district * post_treatment",
        time_variable_name="year",
        group_variable_name="district",
        model=cp.pymc_models.LinearRegression(sample_kwargs=sample_kwargs),
    )
    assert isinstance(df, pd.DataFrame)
    assert isinstance(result, cp.pymc_experiments.DifferenceInDifferences)
    assert len(result.idata.posterior.coords["chain"]) == sample_kwargs["chains"]
    assert len(result.idata.posterior.coords["draw"]) == sample_kwargs["draws"]


@pytest.mark.integration
def test_did_banks_multi():
    treatment_time = 1930.5
    df = (
        cp.load_data("banks")
        .filter(items=["bib6", "bib8", "year"])
        .rename(columns={"bib6": "Sixth District", "bib8": "Eighth District"})
        .groupby("year")
        .median()
    )
    # SET TREATMENT TIME TO ZERO =========
    df.index = df.index - treatment_time
    treatment_time = 0
    # ====================================
    df.reset_index(level=0, inplace=True)
    df_long = pd.melt(
        df,
        id_vars=["year"],
        value_vars=["Sixth District", "Eighth District"],
        var_name="district",
        value_name="bib",
    ).sort_values("year")
    df_long["unit"] = df_long["district"]
    df_long["post_treatment"] = df_long.year >= treatment_time
    df_long = df_long.replace({"district": {"Sixth District": 1, "Eighth District": 0}})

    result = cp.pymc_experiments.DifferenceInDifferences(
        df_long,
        formula="bib ~ 1 + year + district + post_treatment + district:post_treatment",
        time_variable_name="year",
        group_variable_name="district",
        model=cp.pymc_models.LinearRegression(sample_kwargs=sample_kwargs),
    )
    assert isinstance(df, pd.DataFrame)
    assert isinstance(result, cp.pymc_experiments.DifferenceInDifferences)
    assert len(result.idata.posterior.coords["chain"]) == sample_kwargs["chains"]
    assert len(result.idata.posterior.coords["draw"]) == sample_kwargs["draws"]


@pytest.mark.integration
def test_rd():
    df = cp.load_data("rd")
    result = cp.pymc_experiments.RegressionDiscontinuity(
        df,
        formula="y ~ 1 + bs(x, df=6) + treated",
        model=cp.pymc_models.LinearRegression(sample_kwargs=sample_kwargs),
        treatment_threshold=0.5,
    )
    assert isinstance(df, pd.DataFrame)
    assert isinstance(result, cp.pymc_experiments.RegressionDiscontinuity)
    assert len(result.idata.posterior.coords["chain"]) == sample_kwargs["chains"]
    assert len(result.idata.posterior.coords["draw"]) == sample_kwargs["draws"]


@pytest.mark.integration
def test_rd_drinking():
    df = (
        cp.load_data("drinking")
        .rename(columns={"agecell": "age"})
        .assign(treated=lambda df_: df_.age > 21)
    )
    result = cp.pymc_experiments.RegressionDiscontinuity(
        df,
        formula="all ~ 1 + age + treated",
        running_variable_name="age",
        model=cp.pymc_models.LinearRegression(sample_kwargs=sample_kwargs),
        treatment_threshold=21,
    )
    assert isinstance(df, pd.DataFrame)
    assert isinstance(result, cp.pymc_experiments.RegressionDiscontinuity)
    assert len(result.idata.posterior.coords["chain"]) == sample_kwargs["chains"]
    assert len(result.idata.posterior.coords["draw"]) == sample_kwargs["draws"]


@pytest.mark.integration
def test_its():
    df = (
        cp.load_data("its")
        .assign(date=lambda x: pd.to_datetime(x["date"]))
        .set_index("date")
    )
    treatment_time = pd.to_datetime("2017-01-01")
    result = cp.pymc_experiments.SyntheticControl(
        df,
        treatment_time,
        formula="y ~ 1 + t + C(month)",
        model=cp.pymc_models.LinearRegression(sample_kwargs=sample_kwargs),
    )
    assert isinstance(df, pd.DataFrame)
    assert isinstance(result, cp.pymc_experiments.SyntheticControl)
    assert len(result.idata.posterior.coords["chain"]) == sample_kwargs["chains"]
    assert len(result.idata.posterior.coords["draw"]) == sample_kwargs["draws"]


@pytest.mark.integration
def test_its_covid():
    df = (
        cp.load_data("covid")
        .assign(date=lambda x: pd.to_datetime(x["date"]))
        .set_index("date")
    )
    treatment_time = pd.to_datetime("2020-01-01")
    result = cp.pymc_experiments.SyntheticControl(
        df,
        treatment_time,
        formula="standardize(deaths) ~ 0 + standardize(t) + C(month) + standardize(temp)",  # noqa E501
        model=cp.pymc_models.LinearRegression(sample_kwargs=sample_kwargs),
    )
    assert isinstance(df, pd.DataFrame)
    assert isinstance(result, cp.pymc_experiments.SyntheticControl)
    assert len(result.idata.posterior.coords["chain"]) == sample_kwargs["chains"]
    assert len(result.idata.posterior.coords["draw"]) == sample_kwargs["draws"]


@pytest.mark.integration
def test_sc():
    df = cp.load_data("sc")
    treatment_time = 70
    result = cp.pymc_experiments.SyntheticControl(
        df,
        treatment_time,
        formula="actual ~ 0 + a + b + c + d + e + f + g",
        model=cp.pymc_models.WeightedSumFitter(sample_kwargs=sample_kwargs),
    )
    assert isinstance(df, pd.DataFrame)
    assert isinstance(result, cp.pymc_experiments.SyntheticControl)
    assert len(result.idata.posterior.coords["chain"]) == sample_kwargs["chains"]
    assert len(result.idata.posterior.coords["draw"]) == sample_kwargs["draws"]


@pytest.mark.integration
def test_sc_brexit():
    df = (
        cp.load_data("brexit")
        .assign(Time=lambda x: pd.to_datetime(x["Time"]))
        .set_index("Time")
        .loc[lambda x: x.index >= "2009-01-01"]
        .drop(["Japan", "Italy", "US", "Spain"], axis=1)
    )
    treatment_time = pd.to_datetime("2016 June 24")
    target_country = "UK"
    all_countries = df.columns
    other_countries = all_countries.difference({target_country})
    all_countries = list(all_countries)
    other_countries = list(other_countries)
    formula = target_country + " ~ " + "0 + " + " + ".join(other_countries)
    result = cp.pymc_experiments.SyntheticControl(
        df,
        treatment_time,
        formula=formula,
        model=cp.pymc_models.WeightedSumFitter(sample_kwargs=sample_kwargs),
    )
    assert isinstance(df, pd.DataFrame)
    assert isinstance(result, cp.pymc_experiments.SyntheticControl)
    assert len(result.idata.posterior.coords["chain"]) == sample_kwargs["chains"]
    assert len(result.idata.posterior.coords["draw"]) == sample_kwargs["draws"]


@pytest.mark.integration
def test_ancova():
    df = cp.load_data("anova1")
    result = cp.pymc_experiments.PrePostNEGD(
        df,
        formula="post ~ 1 + C(group) + pre",
        group_variable_name="group",
        pretreatment_variable_name="pre",
        model=cp.pymc_models.LinearRegression(sample_kwargs=sample_kwargs),
    )
    assert isinstance(df, pd.DataFrame)
    assert isinstance(result, cp.pymc_experiments.PrePostNEGD)
    assert len(result.idata.posterior.coords["chain"]) == sample_kwargs["chains"]
    assert len(result.idata.posterior.coords["draw"]) == sample_kwargs["draws"]


@pytest.mark.integration
def test_geolift1():
    df = (
        cp.load_data("geolift1")
        .assign(time=lambda x: pd.to_datetime(x["time"]))
        .set_index("time")
    )
    treatment_time = pd.to_datetime("2022-01-01")
    result = cp.pymc_experiments.SyntheticControl(
        df,
        treatment_time,
        formula="""Denmark ~ 0 + Austria + Belgium + Bulgaria + Croatia + Cyprus
        + Czech_Republic""",
        model=cp.pymc_models.WeightedSumFitter(sample_kwargs=sample_kwargs),
    )
    assert isinstance(df, pd.DataFrame)
    assert isinstance(result, cp.pymc_experiments.SyntheticControl)
    assert len(result.idata.posterior.coords["chain"]) == sample_kwargs["chains"]
    assert len(result.idata.posterior.coords["draw"]) == sample_kwargs["draws"]
