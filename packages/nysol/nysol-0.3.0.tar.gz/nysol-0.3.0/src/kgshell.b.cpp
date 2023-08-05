/* ////////// LICENSE INFO ////////////////////

 * Copyright (C) 2013 by NYSOL CORPORATION
 *
 * Unless you have received this program directly from NYSOL pursuant
 * to the terms of a commercial license agreement with NYSOL, then
 * this program is licensed to you under the terms of the GNU Affero General
 * Public License (AGPL) as published by the Free Software Foundation,
 * either version 3 of the License, or (at your option) any later version.
 * 
 * This program is distributed in the hope that it will be useful, but
 * WITHOUT ANY EXPRESS OR IMPLIED WARRANTY, INCLUDING THOSE OF 
 * NON-INFRINGEMENT, MERCHANTABILITY OR FITNESS FOR A PARTICULAR PURPOSE.
 *
 * Please refer to the AGPL (http://www.gnu.org/licenses/agpl-3.0.txt)
 * for more details.

 ////////// LICENSE INFO ////////////////////*/
#include <fcntl.h>
#include <kgCSV.h>
#include <kgEnv.h>
#include <kgError.h>
#include <kgMethod.h>
#include <kgshell.h>
#include <kgTempfile.h>
#include <pthread.h>
#include <sys/time.h>
#include <sys/resource.h>
#include <cxxabi.h>

using namespace kgmod;
using namespace kglib;

template <class kgmodTP> 
void kgshell::setMap(std::string name,int runTP){
	_kgmod_map[name] = boost::lambda::bind(boost::lambda::new_ptr<kgmodTP>());
	_kgmod_run[name] = runTP;
	_kgmod_Iinfo[name] = kgmodTP::_ipara;
	_kgmod_Oinfo[name] = kgmodTP::_opara;
}


kgshell::kgshell(int mflg,int rumlim){

	setMap<kgPyfunc>("runfunc",3);
	setMap<kgLoad>("writelist",1);
	setMap<kgLoad>("readlist",2);
	setMap<kg2Tee>("m2tee",0);
	setMap<kgFifo>("mfifo",0);
	setMap<kgExcmd>("cmd",0);
	setMap<kgLoad>("readcsv",0);
	setMap<kgLoad>("writecsv",0);
	setMap<kgLoad>("mstdin",0);
	setMap<kgLoad>("mstdout",0);
	setMap<kgSortchk>("msortchk",0);
	setMap<kgFifo>("mread",0);
	setMap<kgFifo>("mwrite",0);

	setMap<kgCut>("mcut",0);
	setMap<kgCat>("mcat",0);
	setMap<kgSum>("msum",0);
	setMap<kgCal>("mcal",0);
	setMap<kgJoin>("mjoin",0);
	setMap<kg2Cross>("m2cross",0);
	setMap<kgAccum>("maccum",0);
	setMap<kgAvg>("mavg",0);
	setMap<kgBest>("mbest",0);
	setMap<kgBucket>("mbucket",0);
	setMap<kgChgnum>("mchgnum",0);
	setMap<kgChgstr>("mchgstr",0);
	setMap<kgCombi>("mcombi",0);
	setMap<kgCommon>("mcommon",0);
	setMap<kgCount>("mcount",0);
	setMap<kgCross>("mcross",0);
	setMap<kgDelnull>("mdelnull",0);
	setMap<kgDformat>("mdformat",0);
	setMap<kgDuprec>("mduprec",0);
	setMap<kgFldname>("mfldname",0);
	setMap<kgFsort>("mfsort",0);
	setMap<kgHashavg>("mhashavg",0);
	setMap<kgHashsum>("mhashsum",0);
	setMap<kgKeybreak>("mkeybreak",0);
	setMap<kgMbucket>("mmbucket",0);
	setMap<kgMvavg>("mmvavg",0);
	setMap<kgMvsim>("mmvsim",0);
	setMap<kgMvstats>("mmvstats",0);
	setMap<kgNewnumber>("mnewnumber",0);
	setMap<kgNewrand>("mnewrand",0);
	setMap<kgNewstr>("mnewstr",0);
	setMap<kgNjoin>("mnjoin",0);
	setMap<kgNormalize>("mnormalize",0);
	setMap<kgNrcommon>("mnrcommon",0);
	setMap<kgNrjoin>("mnrjoin",0);
	setMap<kgNullto>("mnullto",0);
	setMap<kgNumber>("mnumber",0);
	setMap<kgPadding>("mpadding",0);
	setMap<kgPaste>("mpaste",0);
	setMap<kgProduct>("mproduct",0);
	setMap<kgRand>("mrand",0);
	setMap<kgRjoin>("mrjoin",0);
	setMap<kgSed>("msed",0);
	setMap<kgSel>("msel",0);
	setMap<kgSelnum>("mselnum",0);
	setMap<kgSelrand>("mselrand",0);
	setMap<kgSelstr>("mselstr",0);
	setMap<kgSetstr>("msetstr",0);
	setMap<kgShare>("mshare",0);
	setMap<kgSim>("msim",0);
	setMap<kgSlide>("mslide",0);
	setMap<kgSplit>("msplit",0);
	setMap<kgStats>("mstats",0);
	setMap<kgSummary>("msummary",0);
	setMap<kgTonull>("mtonull",0);
	setMap<kgTra>("mtra",0);
	setMap<kgTraflg>("mtraflg",0);
	setMap<kgTrafld>("mtrafld",0);
	setMap<kgUniq>("muniq",0);
	setMap<kgVcat>("mvcat",0);
	setMap<kgVcommon>("mvcommon",0);
	setMap<kgVcount>("mvcount",0);
	setMap<kgVdelim>("mvdelim",0);
	setMap<kgVdelnull>("mvdelnull",0);
	setMap<kgVjoin>("mvjoin",0);
	setMap<kgVnullto>("mvnullto",0);
	setMap<kgVreplace>("mvreplace",0);
	setMap<kgVsort>("mvsort",0);
	setMap<kgVuniq>("mvuniq",0);
	setMap<kgWindow>("mwindow",0);
	setMap<kgArff2csv>("marff2csv",0);
	setMap<kgXml2csv>("mxml2csv",0);
	setMap<kgSortf>("msortf",0);
	setMap<kgTab2csv>("mtab2csv",0);
	setMap<kgSep>("msep",0);
	setMap<kgShuffle>("mshuffle",0);
	setMap<kg2Cat>("m2cat",0);
	setMap<kgUnicat>("municat",0);


/*
		_kgmod_map["m2tee"]			= boost::lambda::bind(boost::lambda::new_ptr<kg2Tee>());
		_kgmod_map["mfifo"]			= boost::lambda::bind(boost::lambda::new_ptr<kgFifo>());
		_kgmod_map["cmd"]				= boost::lambda::bind(boost::lambda::new_ptr<kgExcmd>());
		_kgmod_map["runfunc"]		= boost::lambda::bind(boost::lambda::new_ptr<kgPyfunc>());
		_kgmod_map["writelist"]	= boost::lambda::bind(boost::lambda::new_ptr<kgLoad>());
		_kgmod_map["readlist"]	= boost::lambda::bind(boost::lambda::new_ptr<kgLoad>());
		_kgmod_map["readcsv"]		= boost::lambda::bind(boost::lambda::new_ptr<kgLoad>());
		_kgmod_map["writecsv"]	= boost::lambda::bind(boost::lambda::new_ptr<kgLoad>());
		_kgmod_map["mstdin"]		= boost::lambda::bind(boost::lambda::new_ptr<kgLoad>());
		_kgmod_map["mstdout"]		= boost::lambda::bind(boost::lambda::new_ptr<kgLoad>());
		_kgmod_map["msortchk"]	= boost::lambda::bind(boost::lambda::new_ptr<kgSortchk>());
		_kgmod_map["mread"]			= boost::lambda::bind(boost::lambda::new_ptr<kgFifo>());
		_kgmod_map["mwrite"]		= boost::lambda::bind(boost::lambda::new_ptr<kgFifo>());

		_kgmod_map["mcut"]    = boost::lambda::bind(boost::lambda::new_ptr<kgCut>());
		_kgmod_map["mcat"]    = boost::lambda::bind(boost::lambda::new_ptr<kgCat>());
		_kgmod_map["msum"]    = boost::lambda::bind(boost::lambda::new_ptr<kgSum>());
		_kgmod_map["mcal"]    = boost::lambda::bind(boost::lambda::new_ptr<kgCal>());
		_kgmod_map["mjoin"]   = boost::lambda::bind(boost::lambda::new_ptr<kgJoin>());
		_kgmod_map["m2cross"] = boost::lambda::bind(boost::lambda::new_ptr<kg2Cross>());
		_kgmod_map["maccum"]  = boost::lambda::bind(boost::lambda::new_ptr<kgAccum>());
		_kgmod_map["mavg"]    = boost::lambda::bind(boost::lambda::new_ptr<kgAvg>());
		_kgmod_map["mbest"]   = boost::lambda::bind(boost::lambda::new_ptr<kgBest>());
		_kgmod_map["mbucket"] = boost::lambda::bind(boost::lambda::new_ptr<kgBucket>());
		_kgmod_map["mchgnum"] = boost::lambda::bind(boost::lambda::new_ptr<kgChgnum>());
		_kgmod_map["mchgstr"] = boost::lambda::bind(boost::lambda::new_ptr<kgChgstr>());
		_kgmod_map["mcombi"]  = boost::lambda::bind(boost::lambda::new_ptr<kgCombi>());
		_kgmod_map["mcommon"] = boost::lambda::bind(boost::lambda::new_ptr<kgCommon>());
		_kgmod_map["mcount"]  = boost::lambda::bind(boost::lambda::new_ptr<kgCount>());
		_kgmod_map["mcross"]  = boost::lambda::bind(boost::lambda::new_ptr<kgCross>());
		_kgmod_map["mdelnull"] = boost::lambda::bind(boost::lambda::new_ptr<kgDelnull>());
		_kgmod_map["mdformat"] = boost::lambda::bind(boost::lambda::new_ptr<kgDformat>());
		_kgmod_map["mduprec"] = boost::lambda::bind(boost::lambda::new_ptr<kgDuprec>());
		_kgmod_map["mfldname"] = boost::lambda::bind(boost::lambda::new_ptr<kgFldname>());
		_kgmod_map["mfsort"]   = boost::lambda::bind(boost::lambda::new_ptr<kgFsort>());
		_kgmod_map["mhashavg"] = boost::lambda::bind(boost::lambda::new_ptr<kgHashavg>());
		_kgmod_map["mhashsum"] = boost::lambda::bind(boost::lambda::new_ptr<kgHashsum>());
		_kgmod_map["mkeybreak"] = boost::lambda::bind(boost::lambda::new_ptr<kgKeybreak>());
		_kgmod_map["mmbucket"] = boost::lambda::bind(boost::lambda::new_ptr<kgMbucket>());
		_kgmod_map["mmvavg"] = boost::lambda::bind(boost::lambda::new_ptr<kgMvavg>());
		_kgmod_map["mmvsim"] = boost::lambda::bind(boost::lambda::new_ptr<kgMvsim>());
		_kgmod_map["mmvstats"]   = boost::lambda::bind(boost::lambda::new_ptr<kgMvstats>());
		_kgmod_map["mnewnumber"] = boost::lambda::bind(boost::lambda::new_ptr<kgNewnumber>());
		_kgmod_map["mnewrand"]   = boost::lambda::bind(boost::lambda::new_ptr<kgNewrand>());
		_kgmod_map["mnewstr"]    = boost::lambda::bind(boost::lambda::new_ptr<kgNewstr>());
		_kgmod_map["mnjoin"]     = boost::lambda::bind(boost::lambda::new_ptr<kgNjoin>());
		_kgmod_map["mnormalize"] = boost::lambda::bind(boost::lambda::new_ptr<kgNormalize>());
		_kgmod_map["mnrcommon"]  = boost::lambda::bind(boost::lambda::new_ptr<kgNrcommon>());
		_kgmod_map["mnrjoin"]    = boost::lambda::bind(boost::lambda::new_ptr<kgNrjoin>());
		_kgmod_map["mnullto"]    = boost::lambda::bind(boost::lambda::new_ptr<kgNullto>());
		_kgmod_map["mnumber"]    = boost::lambda::bind(boost::lambda::new_ptr<kgNumber>());
		_kgmod_map["mpadding"]   = boost::lambda::bind(boost::lambda::new_ptr<kgPadding>());
		_kgmod_map["mpaste"]     = boost::lambda::bind(boost::lambda::new_ptr<kgPaste>());
		_kgmod_map["mproduct"] = boost::lambda::bind(boost::lambda::new_ptr<kgProduct>());
		_kgmod_map["mrand"]			= boost::lambda::bind(boost::lambda::new_ptr<kgRand>());
		_kgmod_map["mrjoin"]		= boost::lambda::bind(boost::lambda::new_ptr<kgRjoin>());
		_kgmod_map["msed"]			= boost::lambda::bind(boost::lambda::new_ptr<kgSed>());
		_kgmod_map["msel"]			= boost::lambda::bind(boost::lambda::new_ptr<kgSel>());
		_kgmod_map["mselnum"]		= boost::lambda::bind(boost::lambda::new_ptr<kgSelnum>());
		_kgmod_map["mselrand"]	= boost::lambda::bind(boost::lambda::new_ptr<kgSelrand>());
		_kgmod_map["mselstr"]		= boost::lambda::bind(boost::lambda::new_ptr<kgSelstr>());
		_kgmod_map["msetstr"]		= boost::lambda::bind(boost::lambda::new_ptr<kgSetstr>());
		_kgmod_map["mshare"]		= boost::lambda::bind(boost::lambda::new_ptr<kgShare>());
		_kgmod_map["msim"]			= boost::lambda::bind(boost::lambda::new_ptr<kgSim>());
		_kgmod_map["mslide"]		= boost::lambda::bind(boost::lambda::new_ptr<kgSlide>());
		_kgmod_map["msplit"] 		= boost::lambda::bind(boost::lambda::new_ptr<kgSplit>());
		_kgmod_map["mstats"]		= boost::lambda::bind(boost::lambda::new_ptr<kgStats>());
		_kgmod_map["msummary"] 	= boost::lambda::bind(boost::lambda::new_ptr<kgSummary>());
		_kgmod_map["mtonull"]		= boost::lambda::bind(boost::lambda::new_ptr<kgTonull>());
		_kgmod_map["mtra"]			= boost::lambda::bind(boost::lambda::new_ptr<kgTra>());
		_kgmod_map["mtraflg"]		= boost::lambda::bind(boost::lambda::new_ptr<kgTraflg>());
		_kgmod_map["mtrafld"]		= boost::lambda::bind(boost::lambda::new_ptr<kgTrafld>());
		_kgmod_map["muniq"]			= boost::lambda::bind(boost::lambda::new_ptr<kgUniq>());
		_kgmod_map["mvcat"]			= boost::lambda::bind(boost::lambda::new_ptr<kgVcat>());
		_kgmod_map["mvcommon"]	= boost::lambda::bind(boost::lambda::new_ptr<kgVcommon>());
		_kgmod_map["mvcount"]		= boost::lambda::bind(boost::lambda::new_ptr<kgVcount>());
		_kgmod_map["mvdelim"]		= boost::lambda::bind(boost::lambda::new_ptr<kgVdelim>());
		_kgmod_map["mvdelnull"] = boost::lambda::bind(boost::lambda::new_ptr<kgVdelnull>());
		_kgmod_map["mvjoin"]		= boost::lambda::bind(boost::lambda::new_ptr<kgVjoin>());
		_kgmod_map["mvnullto"]	= boost::lambda::bind(boost::lambda::new_ptr<kgVnullto>());
		_kgmod_map["mvreplace"]	= boost::lambda::bind(boost::lambda::new_ptr<kgVreplace>());
		_kgmod_map["mvsort"]		= boost::lambda::bind(boost::lambda::new_ptr<kgVsort>());
		_kgmod_map["mvuniq"]		= boost::lambda::bind(boost::lambda::new_ptr<kgVuniq>());
		_kgmod_map["mwindow"]		= boost::lambda::bind(boost::lambda::new_ptr<kgWindow>());
		_kgmod_map["marff2csv"]	= boost::lambda::bind(boost::lambda::new_ptr<kgArff2csv>());
		_kgmod_map["mxml2csv"]	= boost::lambda::bind(boost::lambda::new_ptr<kgXml2csv>());
		_kgmod_map["msortf"]		= boost::lambda::bind(boost::lambda::new_ptr<kgSortf>());
		_kgmod_map["mtab2csv"]	= boost::lambda::bind(boost::lambda::new_ptr<kgTab2csv>());
		_kgmod_map["msep"]			= boost::lambda::bind(boost::lambda::new_ptr<kgSep>());
		_kgmod_map["mshuffle"]  = boost::lambda::bind(boost::lambda::new_ptr<kgShuffle>());
		_kgmod_map["m2cat"]			= boost::lambda::bind(boost::lambda::new_ptr<kg2Cat>());
		_kgmod_map["municat"]		= boost::lambda::bind(boost::lambda::new_ptr<kgUnicat>());

		_kgmod_run["m2tee"] = 0;
		_kgmod_run["mfifo"] = 0;
		_kgmod_run["mcut"] = 0;
		_kgmod_run["cmd"] = 0;
		_kgmod_run["mcat"] = 0;
		_kgmod_run["msum"] = 0;
		_kgmod_run["mcal"] = 0;
		_kgmod_run["mjoin"] = 0;
		_kgmod_run["m2cross"] = 0;
		_kgmod_run["maccum"] = 0;
		_kgmod_run["mavg"] = 0;
		_kgmod_run["mbest"] = 0;
		_kgmod_run["mbucket"] = 0;
		_kgmod_run["mchgnum"] = 0;
		_kgmod_run["mchgstr"] = 0;
		_kgmod_run["mcombi"] = 0;
		_kgmod_run["mcommon"] = 0;
		_kgmod_run["mcount"] = 0;
		_kgmod_run["mcross"] = 0;
		_kgmod_run["mdelnull"] = 0;
		_kgmod_run["mdformat"] = 0;
		_kgmod_run["mduprec"] = 0;
		_kgmod_run["mfldname"] = 0;
		_kgmod_run["mfsort"] = 0;
		_kgmod_run["mhashavg"] = 0;
		_kgmod_run["mhashsum"] = 0;
		_kgmod_run["mkeybreak"] = 0;
		_kgmod_run["mmbucket"] = 0;
		_kgmod_run["mmvavg"] = 0;
		_kgmod_run["mmvsim"] = 0;
		_kgmod_run["mmvstats"] = 0;
		_kgmod_run["mnewnumber"] = 0;
		_kgmod_run["mnewrand"] = 0;
		_kgmod_run["mnewstr"] = 0;
		_kgmod_run["mnjoin"] = 0;
		_kgmod_run["mnormalize"] = 0;
		_kgmod_run["mnrcommon"] = 0;
		_kgmod_run["mnrjoin"] = 0;
		_kgmod_run["mnullto"] = 0;
		_kgmod_run["mnumber"] = 0;
		_kgmod_run["mpadding"] = 0;
		_kgmod_run["mpaste"] = 0;
		_kgmod_run["mproduct"] = 0;
		_kgmod_run["mrand"] = 0;
		_kgmod_run["mrjoin"] = 0;
		_kgmod_run["msed"] = 0;
		_kgmod_run["msel"] = 0;
		_kgmod_run["mselnum"] = 0;
		_kgmod_run["mselrand"] = 0;
		_kgmod_run["mselstr"] = 0;
		_kgmod_run["msep"] = 0;
		_kgmod_run["mshuffle"] = 0;
		_kgmod_run["msetstr"] = 0;
		_kgmod_run["mshare"] = 0;
		_kgmod_run["msim"] = 0;
		_kgmod_run["mslide"] = 0;
		_kgmod_run["msplit"] = 0;
		_kgmod_run["mstats"] = 0;
		_kgmod_run["msummary"] = 0;
		_kgmod_run["mtonull"] = 0;
		_kgmod_run["mtra"] = 0;
		_kgmod_run["mtraflg"] = 0;
		_kgmod_run["mtrafld"] = 0;
		_kgmod_run["muniq"] = 0;
		_kgmod_run["mvcat"] = 0;
		_kgmod_run["mvcommon"] = 0;
		_kgmod_run["mvcount"] = 0;
		_kgmod_run["mvdelim"] = 0;
		_kgmod_run["mvdelnull"] = 0;
		_kgmod_run["mvjoin"] = 0;
		_kgmod_run["mvnullto"] = 0;
		_kgmod_run["mvreplace"] = 0;
		_kgmod_run["mvsort"] = 0;
		_kgmod_run["mvuniq"] = 0;
		_kgmod_run["mwindow"] = 0;
		_kgmod_run["marff2csv"] =0;
		_kgmod_run["mxml2csv"] =0;
		_kgmod_run["msortf"] =0;
		_kgmod_run["mtab2csv"] = 0;
		_kgmod_run["writecsv"] = 0;
		_kgmod_run["readcsv"] = 0;
		_kgmod_run["runfunc"] = 3;
		_kgmod_run["mstdin"] = 0;
		_kgmod_run["mstdout"] = 0;
		_kgmod_run["m2cat"] = 0;
		_kgmod_run["msortchk"] = 0;
		_kgmod_run["municat"] = 0;

		_kgmod_run["mread"] = 0;
		_kgmod_run["mwrite"] = 0;
		_kgmod_run["writelist"] = 1;
		_kgmod_run["readlist"] = 2;

		//splitToken(string,..)はあとで除く
		_kgmod_Iinfo["m2tee"] = kg2Tee::_ipara;
		_kgmod_Iinfo["mfifo"] = kgFifo::_ipara;
		_kgmod_Iinfo["mcut"] = kgCut::_ipara;
		_kgmod_Iinfo["cmd"] = kgExcmd::_ipara;
		_kgmod_Iinfo["mcat"] = kgCat::_ipara;
		_kgmod_Iinfo["msum"] = kgSum::_ipara;
		_kgmod_Iinfo["mcal"] = kgCal::_ipara;
		_kgmod_Iinfo["mjoin"] = kgJoin::_ipara;
		_kgmod_Iinfo["m2cross"] = kg2Cross::_ipara;
		_kgmod_Iinfo["maccum"] = kgAccum::_ipara;
		_kgmod_Iinfo["mavg"] = kgAvg::_ipara;
		_kgmod_Iinfo["mbest"] = kgBest::_ipara;
		_kgmod_Iinfo["mbucket"] = kgBucket::_ipara;
		_kgmod_Iinfo["mchgnum"] = kgChgnum::_ipara;
		_kgmod_Iinfo["mchgstr"] = kgChgstr::_ipara;
		_kgmod_Iinfo["mcombi"] = kgCombi::_ipara;
		_kgmod_Iinfo["mcommon"] = kgCommon::_ipara;
		_kgmod_Iinfo["mcount"] = kgCount::_ipara;
		_kgmod_Iinfo["mcross"] = kgCross::_ipara;
		_kgmod_Iinfo["mdelnull"] = kgDelnull::_ipara;
		_kgmod_Iinfo["mdformat"] = kgDformat::_ipara;
		_kgmod_Iinfo["mduprec"] = kgDuprec::_ipara;
		_kgmod_Iinfo["mfldname"] = kgFldname::_ipara;
		_kgmod_Iinfo["mfsort"] = kgFsort::_ipara;
		_kgmod_Iinfo["mhashavg"] = kgHashavg::_ipara;
		_kgmod_Iinfo["mhashsum"] = kgHashsum::_ipara;
		_kgmod_Iinfo["mkeybreak"] = kgKeybreak::_ipara;
		_kgmod_Iinfo["mmbucket"] = kgMbucket::_ipara;
		_kgmod_Iinfo["mmvavg"] = kgMvavg::_ipara;
		_kgmod_Iinfo["mmvsim"] = kgMvsim::_ipara;
		_kgmod_Iinfo["mmvstats"] = kgMvstats::_ipara;
		_kgmod_Iinfo["mnewnumber"] = kgNewnumber::_ipara;
		_kgmod_Iinfo["mnewrand"] = kgNewrand::_ipara;
		_kgmod_Iinfo["mnewstr"] = kgNewstr::_ipara;
		_kgmod_Iinfo["mnjoin"] = kgNjoin::_ipara;
		_kgmod_Iinfo["mnormalize"] = kgNormalize::_ipara;
		_kgmod_Iinfo["mnrcommon"] = kgNrcommon::_ipara;
		_kgmod_Iinfo["mnrjoin"] = kgNrjoin::_ipara;
		_kgmod_Iinfo["mnullto"] = kgNullto::_ipara;
		_kgmod_Iinfo["mnumber"] = kgNumber::_ipara;
		_kgmod_Iinfo["mpadding"] = kgPadding::_ipara;
		_kgmod_Iinfo["mpaste"] = kgPaste::_ipara;
		_kgmod_Iinfo["mproduct"] = kgProduct::_ipara;
		_kgmod_Iinfo["mrand"] = kgRand::_ipara;
		_kgmod_Iinfo["mrjoin"] = kgRjoin::_ipara;
		_kgmod_Iinfo["msed"] = kgSed::_ipara;
		_kgmod_Iinfo["msel"] = kgSel::_ipara;
		_kgmod_Iinfo["mselnum"] = kgSelnum::_ipara;
		_kgmod_Iinfo["mselrand"] = kgSelrand::_ipara;
		_kgmod_Iinfo["mselstr"] = kgSelstr::_ipara;
		_kgmod_Iinfo["msep"] = kgSep::_ipara;
		_kgmod_Iinfo["mshuffle"] = kgShuffle::_ipara;
		_kgmod_Iinfo["msetstr"] = kgSetstr::_ipara;
		_kgmod_Iinfo["mshare"] = kgShare::_ipara;
		_kgmod_Iinfo["msim"] = kgSim::_ipara;
		_kgmod_Iinfo["mslide"] = kgSlide::_ipara;
		_kgmod_Iinfo["msplit"] = kgSplit::_ipara;
		_kgmod_Iinfo["mstats"] = kgStats::_ipara;
		_kgmod_Iinfo["msummary"] = kgSummary::_ipara;
		_kgmod_Iinfo["mtonull"] = kgTonull::_ipara;
		_kgmod_Iinfo["mtra"]    = kgTra::_ipara;
		_kgmod_Iinfo["mtraflg"] = kgTraflg::_ipara;
		_kgmod_Iinfo["mtrafld"] = kgTrafld::_ipara;
		_kgmod_Iinfo["muniq"]   = kgUniq::_ipara;
		_kgmod_Iinfo["mvcat"]   = kgVcat::_ipara;
		_kgmod_Iinfo["mvcommon"]  = kgVcommon::_ipara;
		_kgmod_Iinfo["mvcount"]   = kgVcount::_ipara;
		_kgmod_Iinfo["mvdelim"]   = kgVdelim::_ipara;
		_kgmod_Iinfo["mvdelnull"] = kgVdelnull::_ipara;
		_kgmod_Iinfo["mvjoin"]    = kgVjoin::_ipara;
		_kgmod_Iinfo["mvnullto"]  = kgVnullto::_ipara;
		_kgmod_Iinfo["mvreplace"] = kgVreplace::_ipara;
		_kgmod_Iinfo["mvsort"]   = kgVsort::_ipara;
		_kgmod_Iinfo["mvuniq"]   = kgVuniq::_ipara;
		_kgmod_Iinfo["mwindow"]  = kgWindow::_ipara;
		_kgmod_Iinfo["marff2csv"] = kgArff2csv::_ipara;
		_kgmod_Iinfo["mxml2csv"] = kgXml2csv::_ipara;
		_kgmod_Iinfo["msortf"]   = kgSortf::_ipara;
		_kgmod_Iinfo["mtab2csv"] = kgTab2csv::_ipara;
		_kgmod_Iinfo["writecsv"] = kgLoad::_ipara;
		_kgmod_Iinfo["readcsv"]  = kgLoad::_ipara;
		_kgmod_Iinfo["runfunc"]  = kgPyfunc::_ipara;
		_kgmod_Iinfo["mstdin"]   = kgLoad::_ipara;
		_kgmod_Iinfo["mstdout"]  = kgLoad::_ipara;
		_kgmod_Iinfo["m2cat"]    = kg2Cat::_ipara;
		_kgmod_Iinfo["msortchk"] = kgSortchk::_ipara;
		_kgmod_Iinfo["municat"]  = kgUnicat::_ipara;
		_kgmod_Iinfo["mread"]     = kgFifo::_ipara;
		_kgmod_Iinfo["mwrite"]    = kgFifo::_ipara;
		_kgmod_Iinfo["writelist"] = kgLoad::_ipara;
		_kgmod_Iinfo["readlist"]  = kgLoad::_ipara;

		_kgmod_Oinfo["m2tee"] = kg2Tee::_opara;
		_kgmod_Oinfo["mfifo"] = kgFifo::_opara;
		_kgmod_Oinfo["mcut"] = kgCut::_opara;
		_kgmod_Oinfo["cmd"] = kgExcmd::_opara;
		_kgmod_Oinfo["mcat"] = kgCat::_opara;
		_kgmod_Oinfo["msum"] = kgSum::_opara;
		_kgmod_Oinfo["mcal"] = kgCal::_opara;
		_kgmod_Oinfo["mjoin"] = kgJoin::_opara;
		_kgmod_Oinfo["m2cross"] = kg2Cross::_opara;
		_kgmod_Oinfo["maccum"] = kgAccum::_opara;
		_kgmod_Oinfo["mavg"] =   kgAvg::_opara;
		_kgmod_Oinfo["mbest"] = kgBest::_opara;
		_kgmod_Oinfo["mbucket"] = kgBucket::_opara;
		_kgmod_Oinfo["mchgnum"] = kgChgnum::_opara;
		_kgmod_Oinfo["mchgstr"] = kgChgstr::_opara;
		_kgmod_Oinfo["mcombi"] = kgCombi::_opara;
		_kgmod_Oinfo["mcommon"] = kgCommon::_opara;
		_kgmod_Oinfo["mcount"] = kgCount::_opara;
		_kgmod_Oinfo["mcross"] = kgCross::_opara;
		_kgmod_Oinfo["mdelnull"] = kgDelnull::_opara;
		_kgmod_Oinfo["mdformat"] = kgDformat::_opara;
		_kgmod_Oinfo["mduprec"] = kgDuprec::_opara;
		_kgmod_Oinfo["mfldname"] = kgFldname::_opara;
		_kgmod_Oinfo["mfsort"] = kgFsort::_opara;
		_kgmod_Oinfo["mhashavg"] = kgHashavg::_opara;
		_kgmod_Oinfo["mhashsum"] = kgHashsum::_opara;
		_kgmod_Oinfo["mkeybreak"] = kgKeybreak::_opara;
		_kgmod_Oinfo["mmbucket"] = kgMbucket::_opara;
		_kgmod_Oinfo["mmvavg"] = kgMvavg::_opara;
		_kgmod_Oinfo["mmvsim"] = kgMvsim::_opara;
		_kgmod_Oinfo["mmvstats"] = kgMvstats::_opara;
		_kgmod_Oinfo["mnewnumber"] = kgNewnumber::_opara;
		_kgmod_Oinfo["mnewrand"] = kgNewrand::_opara;
		_kgmod_Oinfo["mnewstr"] = kgNewstr::_opara;
		_kgmod_Oinfo["mnjoin"] = kgNjoin::_opara;
		_kgmod_Oinfo["mnormalize"] = kgNormalize::_opara;
		_kgmod_Oinfo["mnrcommon"] = kgNrcommon::_opara;
		_kgmod_Oinfo["mnrjoin"] = kgNrjoin::_opara;
		_kgmod_Oinfo["mnullto"] = kgNullto::_opara;
		_kgmod_Oinfo["mnumber"] = kgNumber::_opara;
		_kgmod_Oinfo["mpadding"] = kgPadding::_opara;
		_kgmod_Oinfo["mpaste"] = kgPaste::_opara;
		_kgmod_Oinfo["mproduct"] = kgProduct::_opara;
		_kgmod_Oinfo["mrand"] = kgRand::_opara;
		_kgmod_Oinfo["mrjoin"] = kgRjoin::_opara;
		_kgmod_Oinfo["msed"] = kgSed::_opara;
		_kgmod_Oinfo["msel"] = kgSel::_opara;
		_kgmod_Oinfo["mselnum"] = kgSelnum::_opara;
		_kgmod_Oinfo["mselrand"] = kgSelrand::_opara;
		_kgmod_Oinfo["mselstr"] = kgSelstr::_opara;
		_kgmod_Oinfo["msep"] = kgSep::_opara;
		_kgmod_Oinfo["mshuffle"] = kgShuffle::_opara;
		_kgmod_Oinfo["msetstr"] = kgSetstr::_opara;
		_kgmod_Oinfo["mshare"] = kgShare::_opara;
		_kgmod_Oinfo["msim"] = kgSim::_opara;
		_kgmod_Oinfo["mslide"] = kgSlide::_opara;
		_kgmod_Oinfo["msplit"] = kgSplit::_opara;
		_kgmod_Oinfo["mstats"] = kgStats::_opara;
		_kgmod_Oinfo["msummary"] = kgSummary::_opara;
		_kgmod_Oinfo["mtonull"] = kgTonull::_opara;
		_kgmod_Oinfo["mtra"]    = kgTra::_opara;
		_kgmod_Oinfo["mtraflg"] = kgTraflg::_opara;
		_kgmod_Oinfo["mtrafld"] = kgTrafld::_opara;
		_kgmod_Oinfo["muniq"]   = kgUniq::_opara;
		_kgmod_Oinfo["mvcat"]   = kgVcat::_opara;
		_kgmod_Oinfo["mvcommon"]  = kgVcommon::_opara;
		_kgmod_Oinfo["mvcount"]   = kgVcount::_opara;
		_kgmod_Oinfo["mvdelim"]   = kgVdelim::_opara;
		_kgmod_Oinfo["mvdelnull"] = kgVdelnull::_opara;
		_kgmod_Oinfo["mvjoin"]    = kgVjoin::_opara;
		_kgmod_Oinfo["mvnullto"]  = kgVnullto::_opara;
		_kgmod_Oinfo["mvreplace"] = kgVreplace::_opara;
		_kgmod_Oinfo["mvsort"]   = kgVsort::_opara;
		_kgmod_Oinfo["mvuniq"]   = kgVuniq::_opara;
		_kgmod_Oinfo["mwindow"]  = kgWindow::_opara;
		_kgmod_Oinfo["marff2csv"] = kgArff2csv::_opara;
		_kgmod_Oinfo["mxml2csv"] = kgXml2csv::_opara;
		_kgmod_Oinfo["msortf"]   = kgSortf::_opara;
		_kgmod_Oinfo["mtab2csv"] = kgTab2csv::_opara;
		_kgmod_Oinfo["writecsv"] = kgLoad::_opara;
		_kgmod_Oinfo["readcsv"]  = kgLoad::_opara;
		_kgmod_Oinfo["runfunc"]  = kgPyfunc::_opara;
		_kgmod_Oinfo["mstdin"]   = kgLoad::_opara;
		_kgmod_Oinfo["mstdout"]  = kgLoad::_opara;
		_kgmod_Oinfo["m2cat"]    = kg2Cat::_opara;
		_kgmod_Oinfo["msortchk"] = kgSortchk::_opara;
		_kgmod_Oinfo["municat"]  = kgUnicat::_opara;
		_kgmod_Oinfo["mread"]     = kgFifo::_opara;
		_kgmod_Oinfo["mwrite"]    = kgFifo::_opara;
		_kgmod_Oinfo["writelist"] = kgLoad::_opara;
		_kgmod_Oinfo["readlist"]  = kgLoad::_opara;

*/

		_nfni = false;
 		_iterrtn= NULL;
 		_iterrtnk= NULL;
		_th_st_pp = NULL;
		_clen = 0;
		_modlist=NULL;

		if(!mflg){  _env.verblvl(2);	}

		_runlim = rumlim;

	  if (pthread_mutex_init(&_mutex, NULL) == -1) { 
			ostringstream ss;
			ss << "init mutex error";
			throw kgError(ss.str());
	  }
	  if (pthread_mutex_init(&_stsMutex, NULL) == -1) { 
			ostringstream ss;
			ss << "init mutex error";
			throw kgError(ss.str());
	  }

	  if (pthread_cond_init(&_stsCond, NULL) == -1) { 
			ostringstream ss;
			ss << "init cond mutex error";
			throw kgError(ss.str());
	  }
	  
	  if (pthread_cond_init(&_forkCond, NULL) == -1) { 
			ostringstream ss;
			ss << "init cond mutex error";
			throw kgError(ss.str());
	  }
	  
	  
		_tempFile.init(&_env);
}



void *kgshell::run_func(void *arg){

	try{

		string msg;
		argST *a =(argST*)arg; 

		int sts = a->mobj->run(a->i_cnt,a->i_p,a->o_cnt,a->o_p,msg);

		pthread_mutex_lock(a->stMutex);

		a->status =sts;
		a->finflg=true;
		a->msg.append(msg);
		a->endtime=getNowTime(true);

		pthread_cond_signal(a->stCond);
		pthread_mutex_unlock(a->stMutex);

	}
	catch(kgError& err){
		argST *a =(argST*)arg; 
		pthread_mutex_lock(a->stMutex);
		a->status = 1;
		a->finflg=true;
		a->endtime=getNowTime(true);
		a->msg.append(a->mobj->name());
		a->msg.append(" ");
		a->msg.append(err.message(0));
		pthread_cond_signal(a->stCond);
		pthread_mutex_unlock(a->stMutex);

	}catch (const exception& e) {
		argST *a =(argST*)arg; 
		pthread_mutex_lock(a->stMutex);
		a->status = 1;
		a->finflg=true;
		a->endtime=getNowTime(true);
		a->msg.append(a->mobj->name());
		a->msg.append(" ");
		a->msg.append(e.what());
		pthread_cond_signal(a->stCond);
		pthread_mutex_unlock(a->stMutex);

	}catch(char * er){
		argST *a =(argST*)arg; 
		pthread_mutex_lock(a->stMutex);
		a->status = 1;
		a->finflg=true;
		a->endtime=getNowTime(true);
		a->msg.append(a->mobj->name());
		a->msg.append(" ");
		a->msg.append(er);
		pthread_cond_signal(a->stCond);
		pthread_mutex_unlock(a->stMutex);
	}
#if !defined(__clang__) && defined(__GNUC__)
	catch(abi::__forced_unwind&){  
		argST *a =(argST*)arg; 
		pthread_mutex_lock(a->stMutex);
		a->status = 2;
		a->finflg=true;
		a->endtime=getNowTime(true);
		a->msg.append(a->mobj->name());
		a->msg.append(" ABI THROW");
		pthread_cond_signal(a->stCond);
		pthread_mutex_unlock(a->stMutex);
		throw;
	}
#endif
	catch(...){
		argST *a =(argST*)arg; 
		pthread_mutex_lock(a->stMutex);
		a->status = 1;
		a->finflg=true;
		a->endtime=getNowTime(true);
		a->msg.append(a->mobj->name());
		a->msg.append(" unKnown ERROR ");
		pthread_cond_signal(a->stCond);
		pthread_mutex_unlock(a->stMutex);
	}

	pthread_exit(0);

	return NULL;	
}

void *kgshell::run_writelist(void *arg){
	try{
		string msg;
		argST *a =(argST*)arg; 
		int sts = a->mobj->run(a->i_cnt,a->i_p,a->list,a->mutex,msg);
		pthread_mutex_lock(a->stMutex);
		a->status = sts;
		a->finflg=true;
		a->msg.append(msg);
		a->endtime=getNowTime(true);

		pthread_cond_signal(a->stCond);
		pthread_mutex_unlock(a->stMutex);

	}
	catch(kgError& err){
		argST *a =(argST*)arg; 
		pthread_mutex_lock(a->stMutex);
		a->status = 1;
		a->finflg=true;
		a->endtime=getNowTime(true);
		a->msg.append(a->mobj->name());
		a->msg.append(" ");
		a->msg.append(err.message(0));
		pthread_cond_signal(a->stCond);
		pthread_mutex_unlock(a->stMutex);

	}catch (const exception& e) {
		argST *a =(argST*)arg; 
		pthread_mutex_lock(a->stMutex);
		a->status = 1;
		a->finflg=true;
		a->endtime=getNowTime(true);
		a->msg.append(a->mobj->name());
		a->msg.append(" ");
		a->msg.append(e.what());
		pthread_cond_signal(a->stCond);
		pthread_mutex_unlock(a->stMutex);

	}catch(char * er){
		argST *a =(argST*)arg; 
		pthread_mutex_lock(a->stMutex);
		a->status = 1;
		a->finflg=true;
		a->endtime=getNowTime(true);
		a->msg.append(a->mobj->name());
		a->msg.append(" ");
		a->msg.append(er);
		pthread_cond_signal(a->stCond);
		pthread_mutex_unlock(a->stMutex);

	}
#if !defined(__clang__) && defined(__GNUC__)
	catch(abi::__forced_unwind&){  
		argST *a =(argST*)arg; 
		pthread_mutex_lock(a->stMutex);
		a->status = 2;
		a->finflg=true;
		a->endtime=getNowTime(true);
		a->msg.append(a->mobj->name());
		a->msg.append(" ABI THROW");
		pthread_cond_signal(a->stCond);
		pthread_mutex_unlock(a->stMutex);
		throw;
	}
#endif	
	catch(...){
		argST *a =(argST*)arg; 
		pthread_mutex_lock(a->stMutex);
		a->status = 1;
		a->finflg=true;
		a->endtime=getNowTime(true);
		a->msg.append(a->mobj->name());
		a->msg.append(" unKnown ERROR");
		pthread_cond_signal(a->stCond);
		pthread_mutex_unlock(a->stMutex);
	}
	pthread_exit(0);
	return NULL;	
}

void *kgshell::run_readlist(void *arg){
	try{
		string msg;
		argST *a =(argST*)arg; 
		int sts = a->mobj->run(a->list,a->o_cnt,a->o_p,msg);
		pthread_mutex_lock(a->stMutex);
		a->status = sts;
		a->finflg=true;
		a->msg.append(msg);
		a->endtime=getNowTime(true);

		pthread_cond_signal(a->stCond);
		pthread_mutex_unlock(a->stMutex);

	}catch(kgError& err){
		argST *a =(argST*)arg; 
		pthread_mutex_lock(a->stMutex);
		a->status = 1;
		a->finflg=true;
		a->endtime=getNowTime(true);
		a->msg.append(" unKnown ERROR");
		a->msg.append(a->mobj->name());
		a->msg.append(" ");
		a->msg.append(err.message(0));
		pthread_cond_signal(a->stCond);
		pthread_mutex_unlock(a->stMutex);

	}catch (const exception& e) {
		argST *a =(argST*)arg; 
		pthread_mutex_lock(a->stMutex);
		a->status = 1;
		a->finflg=true;
		a->endtime=getNowTime(true);
		a->msg.append(" unKnown ERROR");
		a->msg.append(a->mobj->name());
		a->msg.append(" ");
		a->msg.append(e.what());
		pthread_cond_signal(a->stCond);
		pthread_mutex_unlock(a->stMutex);

	}catch(char * er){
		argST *a =(argST*)arg; 
		pthread_mutex_lock(a->stMutex);
		a->status = 1;
		a->finflg=true;
		a->endtime=getNowTime(true);
		a->msg.append(" unKnown ERROR");
		a->msg.append(a->mobj->name());
		a->msg.append(" ");
		a->msg.append(er);
		pthread_cond_signal(a->stCond);
		pthread_mutex_unlock(a->stMutex);

	}
#if !defined(__clang__) && defined(__GNUC__)
	catch(abi::__forced_unwind&){  
		argST *a =(argST*)arg; 
		pthread_mutex_lock(a->stMutex);
		a->status = 2;
		a->finflg=true;
		a->endtime=getNowTime(true);
		a->msg.append(a->mobj->name());
		a->msg.append(" ABI THROW");
		pthread_cond_signal(a->stCond);
		pthread_mutex_unlock(a->stMutex);
		throw;
	}
#endif	
	catch(...){
		argST *a =(argST*)arg; 
		pthread_mutex_lock(a->stMutex);
		a->status = 1;
		a->finflg=true;
		a->endtime=getNowTime(true);
		a->msg.append(" unKnown ERROR");
		a->msg.append(a->mobj->name());
		pthread_cond_signal(a->stCond);
		pthread_mutex_unlock(a->stMutex);
	}
	pthread_exit(0);
	return NULL;	
}



void *kgshell::run_pyfunc(void *arg){
	try{
		string msg;
		argST *a =(argST*)arg; 

		int sts = a->mobj->run(
			a->fobj,a->aobj,a->kobj,
			a->i_cnt,a->i_p,a->o_cnt,a->o_p,msg,
			a->mutex,a->forkCond,a->runst
		);


		pthread_mutex_lock(a->stMutex);
		a->status = sts;
		a->finflg=true;
		a->msg.append(msg);
		a->endtime=getNowTime(true);

		pthread_cond_signal(a->stCond);
		pthread_mutex_unlock(a->stMutex);

	}catch(kgError& err){
		argST *a =(argST*)arg; 
		pthread_mutex_lock(a->stMutex);
		a->status = 1;
		a->finflg=true;
		a->endtime=getNowTime(true);
		a->msg.append(a->mobj->name());
		a->msg.append(" ");
		a->msg.append(err.message(0));
		pthread_cond_signal(a->stCond);
		pthread_mutex_unlock(a->stMutex);

	}catch (const exception& e) {
		argST *a =(argST*)arg; 
		pthread_mutex_lock(a->stMutex);
		a->status = 1;
		a->finflg=true;
		a->endtime=getNowTime(true);
		a->msg.append(a->mobj->name());
		a->msg.append(" ");
		a->msg.append(e.what());
		pthread_cond_signal(a->stCond);
		pthread_mutex_unlock(a->stMutex);

	}catch(char * er){
		argST *a =(argST*)arg; 
		pthread_mutex_lock(a->stMutex);
		a->status = 1;
		a->finflg=true;
		a->endtime=getNowTime(true);
		a->msg.append(a->mobj->name());
		a->msg.append(" ");
		a->msg.append(er);
		pthread_cond_signal(a->stCond);
		pthread_mutex_unlock(a->stMutex);

	}
#if !defined(__clang__) && defined(__GNUC__)
	catch(abi::__forced_unwind&){  
		argST *a =(argST*)arg; 
		pthread_mutex_lock(a->stMutex);
		a->status = 2;
		a->finflg=true;
		a->endtime=getNowTime(true);
		a->msg.append(a->mobj->name());
		a->msg.append(" ABI THROW");
		pthread_cond_signal(a->stCond);
		pthread_mutex_unlock(a->stMutex);
		throw;
	}
#endif	
	catch(...){
		argST *a =(argST*)arg; 
		pthread_mutex_lock(a->stMutex);
		a->status = 1;
		a->finflg=true;
		a->endtime=getNowTime(true);
		a->msg.append(a->mobj->name());
		a->msg.append(" unKnown ERROR");
		pthread_cond_signal(a->stCond);
		pthread_mutex_unlock(a->stMutex);
	}
	pthread_exit(0);

	return NULL;	
}

void kgshell::raw_OUTPUT(const string& v){
	kgMsg msg(kgMsg::IGN, &_env);
	msg.output_ignore(v);
}

void kgshell::end_OUTPUT(const string& v){
	kgMsg msg(kgMsg::END, &_env);
	ostringstream ss;
	ss << "kgshell (" << v << ")"; 
	msg.output(ss.str());

}
void kgshell::war_OUTPUT(const string& v){
	kgMsg msg(kgMsg::WAR, &_env);
	ostringstream ss;
	ss << "kgshell (" << v << ")";
	msg.output(ss.str());
}
void kgshell::err_OUTPUT(const string& v){
	kgMsg msg(kgMsg::ERR, &_env);	
	ostringstream ss;
	ss << "kgshell (" << v << ")";
	msg.output(ss.str());
}

void kgshell::makePipeList(vector<linkST> & plist,int iblk)
{

	_ipipe_map.clear();
	_opipe_map.clear();
	_FDlist.clear();
	
	//int pcnt = _spblk.getLinkBlkSize_M(iblk);
	int pcnt = _spblk.getModBlkSize_M(iblk);

	rlimit rlim;
	int chfFlg;
	chfFlg = getrlimit(RLIMIT_NOFILE, &rlim);
	size_t pfilecnt = pcnt * 32 ;
	if(rlim.rlim_cur < pfilecnt ){
		rlim.rlim_cur = pfilecnt;
		chfFlg = setrlimit(RLIMIT_NOFILE, &rlim);
		if (chfFlg <0 ) { 
			throw kgError("change file limit on kgshell"); 
		}
	}

	vector<int> linklist = _spblk.getLinkBlkInfo_M(iblk);

	for(size_t j=0;j<linklist.size();j++){
		int i = linklist[j];
		
		int piped[2];
		if( pipe(piped) < 0){ throw kgError("pipe open error on kgshell :("+toString(errno)+")");}
		int flags0 = fcntl(piped[0], F_GETFD);
		int flags1 = fcntl(piped[1], F_GETFD);
		fcntl(piped[0], F_SETFD, flags0 | FD_CLOEXEC);
		fcntl(piped[1], F_SETFD, flags1 | FD_CLOEXEC);
		_FDlist.push_back(piped[0]);
		_FDlist.push_back(piped[1]);


		/*linkST{ kgstr_t frTP; int frID; kgstr_t toTP; int toID;};*/
		//typedef map<int, map<string,vector<int> > > iomap_t;
		
		if ( _ipipe_map.find(plist[i].toID) == _ipipe_map.end()){
			map< string,vector<int> > newmap;
			_ipipe_map[plist[i].toID] = newmap; 
		}
		if ( _ipipe_map[plist[i].toID].find(plist[i].toTP) == _ipipe_map[plist[i].toID].end()){
			vector<int> newvec;
			_ipipe_map[plist[i].toID][plist[i].toTP] = newvec;
		}
		_ipipe_map[plist[i].toID][plist[i].toTP].push_back(piped[0]);

		if ( _opipe_map.find(plist[i].frID) == _opipe_map.end()){
			map< string,vector<int> > newmap;
			_opipe_map[plist[i].frID] = newmap; 
		}
		if ( _opipe_map[plist[i].frID].find(plist[i].frTP) == _opipe_map[plist[i].frID].end()){
			vector<int> newvec;
			_opipe_map[plist[i].frID][plist[i].frTP] = newvec;
		}
		_opipe_map[plist[i].frID][plist[i].frTP].push_back(piped[1]);

	}
}


int kgshell::runMain(vector<cmdCapselST> &cmds,vector<linkST> & plist,int iblk){

	pthread_attr_t pattr;
	char * envStr=getenv("KG_THREAD_STK");
	bool errflg=false;

	size_t stacksize;
	if(envStr!=NULL){
		stacksize = aToSizeT(envStr);
	}else{
		stacksize = KGMOD_THREAD_STK;
	}

	size_t base ;
	int ret = pthread_attr_init(&pattr);
	pthread_attr_getstacksize(&pattr,&base);

	if( stacksize > base ){
		if( pthread_attr_setstacksize(&pattr,stacksize)	){
			err_OUTPUT("stack size change error ");
			return 1;
		}
	}

	makePipeList(plist,iblk);

	_clen = _spblk.getModBlkSize_M(iblk);
	
	//debugIOinfo_OUTPUT(); //DEBUG
	//_clen = cmds.size();

	// initlize
	_modlist = new kgMod*[_clen];
	_argst   = new argST[_clen];
	_runst   = new int[_clen];

	vector<int> cmdlist = _spblk.getModBlkInfo_M(iblk);

	for(size_t i=0;i<cmdlist.size();i++){

		int cmdNo = cmdlist[i];
		if ( _kgmod_map.find(cmds[cmdNo].cmdname) == _kgmod_map.end()){
			err_OUTPUT("not 1 kgmod "+ cmds[cmdNo].cmdname);
			return 1;
		}
		_modlist[i] = _kgmod_map.find(cmds[cmdNo].cmdname)->second() ;
		kgArgs newArgs;
		for(size_t j=0;j<cmds[cmdNo].paralist.size();j++){
			newArgs.add(cmds[cmdNo].paralist[j]);
		}
		_modlist[i]->init(newArgs, &_env);

		_argst[i].mobj= _modlist[i];
		_argst[i].tag= cmds[cmdNo].tag;
		_argst[i].finflg = false;
		_argst[i].outputEND = false;
		_argst[i].status = 0;
		_argst[i].stMutex = &_stsMutex;
		_argst[i].stCond = &_stsCond;
		_argst[i].fobj= cmds[cmdNo].fobj;
		_argst[i].aobj= cmds[cmdNo].aobj;
		_argst[i].kobj= cmds[cmdNo].kobj;
		_argst[i].mutex = &_mutex;
		_argst[i].forkCond = &_forkCond;

		int typ = _kgmod_run.find(cmds[cmdNo].cmdname)->second ;
		if(typ==3){
			_argst[i].fdlist= _FDlist;
			_runst[i] = 0;
		}
		else{
			_runst[i]= 1;
		}
		_argst[i].runst= &(_runst[i]) ;

		if( _ipipe_map.find(cmdNo) == _ipipe_map.end() ){ 
			if(typ==2){
				_argst[i].i_cnt= 1;
				_argst[i].i_p= NULL;
				_argst[i].list = cmds[cmdNo].iobj;
			}
			else{
				_argst[i].i_cnt= 0;
				_argst[i].i_p= NULL;
			}
		}
		else{
			// ここは今のところ固定//全パラメータやる必要＆パラメータ順位をkgmodから
			size_t cnt=0;
			//件数チェック
			if( _kgmod_Iinfo.find(cmds[cmdNo].cmdname) != _kgmod_Iinfo.end()){
				int dmycnt= 0;
				const char ** ikwd = _kgmod_Iinfo.find(cmds[cmdNo].cmdname)->second;
				while(**ikwd){
					if( _ipipe_map[cmdNo].find(*ikwd) != _ipipe_map[cmdNo].end()){
						size_t addcnt = _ipipe_map[cmdNo][*ikwd].size();
						if (addcnt==0){
							dmycnt ++;
						}
						else{
							if(dmycnt!=0){
								cnt += dmycnt;
								dmycnt=0;
							}
							cnt += addcnt;
						}
					}
					else{ dmycnt ++; }
					ikwd++;
				}

/*
				for(size_t ix=0 ; ix < ikwd.size();ix++){
					if( _ipipe_map[cmdNo].find(ikwd[ix]) != _ipipe_map[cmdNo].end()){
						size_t addcnt = _ipipe_map[cmdNo][ikwd[ix]].size();
						if (addcnt==0){
							dmycnt ++;
						}
						else{
							if(dmycnt!=0){
								cnt += dmycnt;
								dmycnt=0;
							}
							cnt += addcnt;
						}
					}
					else{ dmycnt ++; }
				}
*/
			}
			if(cnt==0){
				_argst[i].i_cnt= 0;
				_argst[i].i_p= NULL;
			}
			else{
				//pipeセット
				_argst[i].i_cnt= cnt;
				_argst[i].i_p= new int[cnt];
				for(size_t h=0;h<cnt;h++){
					_argst[i].i_p[h]=-1;
				}
				size_t pos = 0;
				if( _kgmod_Iinfo.find(cmds[cmdNo].cmdname) != _kgmod_Iinfo.end()){
					int dmycnt_s= 0;
					//vector<string> ikwd_s = _kgmod_Iinfo.find(cmds[cmdNo].cmdname)->second;
					const char ** ikwd = _kgmod_Iinfo.find(cmds[cmdNo].cmdname)->second;
					while(**ikwd){
						if( _ipipe_map[cmdNo].find(*ikwd) != _ipipe_map[cmdNo].end()){
							if(_ipipe_map[cmdNo][*ikwd].size()==0){
								dmycnt_s++;
							}
							else{
								pos += dmycnt_s;
							}
							for(size_t jj=0;jj<_ipipe_map[cmdNo][*ikwd].size();jj++){
								_argst[i].i_p[pos] = _ipipe_map[cmdNo][*ikwd][jj];
								pos++;
							}
						}
						else{dmycnt_s++;}
						ikwd++;
					}

/*					for(size_t ixx=0 ; ixx < ikwd_s.size();ixx++){
						if( _ipipe_map[cmdNo].find(ikwd_s[ixx]) != _ipipe_map[cmdNo].end()){
							if(_ipipe_map[cmdNo][ikwd_s[ixx]].size()==0){
								dmycnt_s++;
							}
							else{
								pos += dmycnt_s;
							}
							for(size_t jj=0;jj<_ipipe_map[cmdNo][ikwd_s[ixx]].size();jj++){
								_argst[i].i_p[pos] = _ipipe_map[cmdNo][ikwd_s[ixx]][jj];
								pos++;
							}
						}
						else{dmycnt_s++;}
					}
*/
				}
			}
		}
		if( _opipe_map.find(cmdNo) == _opipe_map.end() ){ 
			if(typ==1){
				_argst[i].o_cnt= 1;
				_argst[i].o_p = NULL;
				_argst[i].mutex = &_mutex;
				_argst[i].list = cmds[cmdNo].oobj;
			}
			else{
				_argst[i].o_cnt= 0;
				_argst[i].o_p= NULL;
			}
		}
		else{

			size_t cnt=0;
			//件数チェック
			if( _kgmod_Oinfo.find(cmds[cmdNo].cmdname) != _kgmod_Oinfo.end()){
				int dmycnt= 0;
				const char ** okwd = _kgmod_Oinfo.find(cmds[cmdNo].cmdname)->second;
				while(**okwd){
					if( _opipe_map[cmdNo].find(*okwd) != _opipe_map[cmdNo].end()){
						size_t addcnt = _opipe_map[cmdNo][*okwd].size();
						if (addcnt==0){
							dmycnt ++;
						}
						else{
							if(dmycnt!=0){
								cnt += dmycnt;
								dmycnt=0;
							}
							cnt += addcnt;
						}
					}
					okwd++;					
				}
				
				/*
				vector<string> okwd = _kgmod_Oinfo.find(cmds[cmdNo].cmdname)->second;
				for(size_t ix=0 ; ix < okwd.size();ix++){
					if( _opipe_map[cmdNo].find(okwd[ix]) != _opipe_map[cmdNo].end()){
						size_t addcnt = _opipe_map[cmdNo][okwd[ix]].size();
						if (addcnt==0){
							dmycnt ++;
						}
						else{
							if(dmycnt!=0){
								cnt += dmycnt;
								dmycnt=0;
							}
							cnt += addcnt;
						}
					}
				}
				*/
			}

			if(cnt==0){
				_argst[i].o_cnt= 0;
				_argst[i].o_p= NULL;
			}
			else{
				_argst[i].o_cnt= cnt;
				_argst[i].o_p= new int[cnt];

				for(size_t h=0;h<cnt;h++){
					_argst[i].o_p[h]=-1;
				}
				size_t pos = 0;
				if( _kgmod_Oinfo.find(cmds[cmdNo].cmdname) != _kgmod_Oinfo.end()){
					int dmycnt_s= 0;
					const char ** okwd_s = _kgmod_Oinfo.find(cmds[cmdNo].cmdname)->second;
					while(**okwd_s){
						if( _opipe_map[cmdNo].find(*okwd_s) != _opipe_map[cmdNo].end()){
							if(_opipe_map[cmdNo][*okwd_s].size()==0){
								dmycnt_s++;
							}
							else{
								pos += dmycnt_s;
							}
							for(size_t jj=0;jj<_opipe_map[cmdNo][*okwd_s].size();jj++){
								_argst[i].o_p[pos] = _opipe_map[cmdNo][*okwd_s][jj];
								pos++;
							}
						}
						okwd_s++;

					}

					/*
					vector<string> okwd_s = _kgmod_Oinfo.find(cmds[cmdNo].cmdname)->second;

					for(size_t ixx=0 ; ixx < okwd_s.size();ixx++){
						if( _opipe_map[cmdNo].find(okwd_s[ixx]) != _opipe_map[cmdNo].end()){
							if(_opipe_map[cmdNo][okwd_s[ixx]].size()==0){
								dmycnt_s++;
							}
							else{
								pos += dmycnt_s;
							}
							for(size_t jj=0;jj<_opipe_map[cmdNo][okwd_s[ixx]].size();jj++){
								_argst[i].o_p[pos] = _opipe_map[cmdNo][okwd_s[ixx]][jj];
								pos++;
							}
						}
					}
					*/
				}
			}
		}
	}

	_th_st_pp = new pthread_t[_clen];
	_th_rtn   = new int[_clen];


	PyThreadState *_save;
	_save = PyEval_SaveThread();

	for(int i=cmdlist.size()-1;i>=0;i--){

		if(3 == _kgmod_run.find(cmds[cmdlist[i]].cmdname)->second){
			pthread_mutex_lock(&_mutex);
			_th_rtn[i] = pthread_create( &_th_st_pp[i], &pattr, kgshell::run_pyfunc ,(void*)&_argst[i]);
			pthread_cond_wait(&_forkCond,&_mutex);
			pthread_mutex_unlock(&_mutex);
		}
	}

	for(int i=cmdlist.size()-1;i>=0;i--){

		//debugARGST_OUTPUT(i);
		if(3 == _kgmod_run.find(cmds[cmdlist[i]].cmdname)->second){
			_runst[i]=1;
		}
	}

	for(int i=cmdlist.size()-1;i>=0;i--){

		//debugARGST_OUTPUT(i);
		int typ = _kgmod_run.find(cmds[cmdlist[i]].cmdname)->second ;

		if(typ==0){
			_th_rtn[i] = pthread_create( &_th_st_pp[i], &pattr, kgshell::run_func ,(void*)&_argst[i]);
		}
		else if(typ==1){
			_th_rtn[i] = pthread_create( &_th_st_pp[i], &pattr, kgshell::run_writelist ,(void*)&_argst[i]);
		}
		else if(typ==2){
			_th_rtn[i] = pthread_create( &_th_st_pp[i], &pattr, kgshell::run_readlist ,(void*)&_argst[i]);
		}
	}

	// status check
	pthread_mutex_lock(&_stsMutex);

	while(1){
		size_t pos = 0;
		bool endFLG = true;
		while(pos<_clen){
			if(_argst[pos].finflg==false){ endFLG=false;}
			else if(_argst[pos].outputEND==false){
				if(!_argst[pos].msg.empty()){
					if(_argst[pos].status==2){
						end_OUTPUT(_argst[pos].msg);
					}
					else{
						raw_OUTPUT(_argst[pos].msg);
					}
				}
				if(!_argst[pos].tag.empty()){
					raw_OUTPUT("#TAG# " + _argst[pos].tag);
				}
				_argst[pos].outputEND = true;
			}
			if(_argst[pos].status!=0&&_argst[pos].status!=2){
 				//エラー発生時はthread cancel
				for(size_t j=0;j<_clen;j++){
					if(!_argst[j].finflg){
						pthread_cancel(_th_st_pp[j]);	
					}
				}
				endFLG=true;
				errflg = true;
				break;
			}
			pos++;
		}
		if (endFLG) break;
		pthread_cond_wait(&_stsCond,&_stsMutex);
	}

	pthread_mutex_unlock(&_stsMutex);

	for(size_t i=_clen;i>0;i--){
		pthread_join(_th_st_pp[i-1],NULL);
	}
	PyEval_RestoreThread(_save);

	if(_modlist){
		for(size_t i=0 ;i<_clen;i++){
			try {
				if(_argst[i].outputEND == false){
					if(!_argst[i].msg.empty()){
						if(_argst[i].status==2){
							end_OUTPUT(_argst[i].msg);
						}
						else{
							raw_OUTPUT(_argst[i].msg);
						}
					}
					if(!_argst[i].tag.empty()){
						raw_OUTPUT("#TAG# " + _argst[i].tag);
					}
				}
				_argst[i].outputEND = true;
				delete _modlist[i];
				_modlist[i] =NULL;
			}
			catch(kgError& err){
				err_OUTPUT("script RUN KGERROR " + err.message(0));
				errflg = true;
			}
			catch(...){ 
				err_OUTPUT("closing.. ");
				errflg = true;
			}
		}
		delete[] _modlist;
	}

	delete[] _th_st_pp;
	delete[] _argst;
	delete[] _th_rtn;
	delete[] _runst;
	_th_st_pp = NULL;
	_argst = NULL;
	_th_rtn = NULL;
	_runst = NULL;
	_modlist = NULL;
	if (errflg) { throw kgError("runmain on kgshell"); }
	return 0;
}


int kgshell::runiter_SUB(vector<cmdCapselST> &cmds,vector<linkST> & plist,int iblk){

	pthread_attr_t pattr;
	char * envStr=getenv("KG_THREAD_STK");

	size_t stacksize;
	if(envStr!=NULL){
		stacksize = aToSizeT(envStr);
	}else{
		stacksize = KGMOD_THREAD_STK;
	}

	size_t base ;
	int ret = pthread_attr_init(&pattr);
	pthread_attr_getstacksize(&pattr,&base);

	if( stacksize > base ){
		if( pthread_attr_setstacksize(&pattr,stacksize)	){
			err_OUTPUT("stack size change error ");
			return -1;
		}
	}

	makePipeList(plist,iblk);

	if( pipe(_csvpiped) < 0){ throw kgError("pipe open error on kgshell");}
	// pipe2(piped,O_CLOEXEC) pipe2なら省略化
	int flags0 = fcntl(_csvpiped[0], F_GETFD);
	int flags1 = fcntl(_csvpiped[1], F_GETFD);
	fcntl(_csvpiped[0], F_SETFD, flags0 | FD_CLOEXEC);
	fcntl(_csvpiped[1], F_SETFD, flags1 | FD_CLOEXEC);


	_clen = _spblk.getModBlkSize_M(iblk);
	
	//debugIOinfo_OUTPUT(); //DEBUG
	//_clen = cmds.size();
	_modlist = new kgMod*[_clen];
	vector<int> cmdlist = _spblk.getModBlkInfo_M(iblk);

	
	int clenpos= 0;
	for(size_t j=0;j<cmdlist.size();j++){

		int i = cmdlist[j];
		if ( _kgmod_map.find(cmds[i].cmdname) == _kgmod_map.end()){
			throw kgError("not kgmod :" + cmds[i].cmdname);
			return -1;
		}
		_modlist[clenpos] = _kgmod_map.find(cmds[i].cmdname)->second() ;
		kgArgs newArgs;
		for(size_t j=0;j<cmds[i].paralist.size();j++){
			newArgs.add(cmds[i].paralist[j]);
		}
		_modlist[clenpos]->init(newArgs, &_env);
		clenpos++;
	}


	_th_st_pp = new pthread_t[clenpos];
	_argst = new argST[clenpos];
	_th_rtn = new int[clenpos];
	int clenpos_a = clenpos;
	// before run 


	for(int j=cmdlist.size()-1;j>=0;j--){

		int i=cmdlist[j];

		clenpos_a--;

		_argst[clenpos_a].mobj= _modlist[clenpos_a];
		_argst[clenpos_a].tag= cmds[i].tag;
		_argst[clenpos_a].finflg = false;
		_argst[clenpos_a].outputEND = false;
		_argst[clenpos_a].status = 0;
		_argst[clenpos_a].stMutex = &_stsMutex;
		_argst[clenpos_a].stCond = &_stsCond;
		_argst[clenpos_a].fobj= cmds[i].fobj;
		_argst[clenpos_a].aobj= cmds[i].aobj;
		_argst[clenpos_a].kobj= cmds[i].kobj;
		_argst[clenpos_a].mutex = &_mutex;

		int typ = _kgmod_run.find(cmds[i].cmdname)->second ;
		if(typ==3){
			_argst[clenpos_a].fdlist= _FDlist;
		}

		if( _ipipe_map.find(i) == _ipipe_map.end() ){ 
			if(typ==2){
				_argst[clenpos_a].i_cnt= 1;
				_argst[clenpos_a].i_p= NULL;
				_argst[clenpos_a].list = cmds[i].iobj;
			}
			else{
				_argst[clenpos_a].i_cnt= 0;
				_argst[clenpos_a].i_p= NULL;
			}
		}
		else{
			// ここは今のところ固定//全パラメータやる必要＆パラメータ順位をkgmodから
			size_t cnt=0;
			if( _ipipe_map[i].find("i") != _ipipe_map[i].end()){
				cnt += _ipipe_map[i]["i"].size();
			}
			if( _ipipe_map[i].find("m") != _ipipe_map[i].end()){
				cnt += _ipipe_map[i]["m"].size();
				if(cnt==1) { cnt++; } //mのみの場合はdmy追加 
			}
			if(cnt==0){
				_argst[clenpos_a].i_cnt= 0;
				_argst[clenpos_a].i_p= NULL;
			}
			else{
				_argst[clenpos_a].i_cnt= cnt;
				_argst[clenpos_a].i_p= new int[cnt];
				size_t pos = 0;
				if( _ipipe_map[i].find("i") != _ipipe_map[i].end()){
					for(size_t j=0;j<_ipipe_map[i]["i"].size();j++){
						_argst[clenpos_a].i_p[pos] = _ipipe_map[i]["i"][j];
						pos++;
					}
				}
				if( _ipipe_map[i].find("m") != _ipipe_map[i].end()){
					if(pos==0 && cnt>1){ // mのみ対応
						_argst[clenpos_a].i_p[pos]=-1; pos++;
					}
					for(size_t j=0;j<_ipipe_map[i]["m"].size();j++){
						_argst[clenpos_a].i_p[pos] = _ipipe_map[i]["m"][j];
						pos++;
					}
				}
			}
		}
		if(i==0){ // kgcsv用
			_argst[i].o_cnt= 1;
			_argst[i].o_p= new int[1];
			_argst[i].o_p[0]= _csvpiped[1]; 
		} 
		else if( _opipe_map.find(i) == _opipe_map.end() ){ 
			if(typ==1){
				_argst[clenpos_a].o_cnt= 1;
				_argst[clenpos_a].o_p = NULL;
				_argst[clenpos_a].mutex = &_mutex;
				_argst[clenpos_a].list = cmds[i].oobj;
			}
			else{
				_argst[clenpos_a].o_cnt= 0;
				_argst[clenpos_a].o_p= NULL;
			}
		}
		else{
			// ここは今のところ固定//全パラメータやる必要＆パラメータ順位をkgmodから
			size_t cnt=0;
			if( _opipe_map[i].find("o") != _opipe_map[i].end()){
				cnt += _opipe_map[i]["o"].size();
			}
			if( _opipe_map[i].find("u") != _ipipe_map[i].end()){
				cnt += _opipe_map[i]["u"].size();
			}
			if(cnt==0){
				_argst[clenpos_a].o_cnt= 0;
				_argst[clenpos_a].o_p= NULL;
			}
			else{
				_argst[clenpos_a].o_cnt= cnt;
				_argst[clenpos_a].o_p= new int[cnt];
				size_t pos = 0;
				if( _opipe_map[i].find("o") != _opipe_map[i].end()){
					for(size_t j=0;j<_opipe_map[i]["o"].size();j++){
					_argst[clenpos_a].o_p[pos] = _opipe_map[i]["o"][j];
						pos++;
					}
				}
				if( _opipe_map[i].find("u") != _opipe_map[i].end()){
					for(size_t j=0;j<_opipe_map[i]["u"].size();j++){
						_argst[clenpos_a].o_p[pos] = _opipe_map[i]["u"][j];
						pos++;
					}
				}
			}
		}

		//debug
			
		//debugARGST_OUTPUT(i);

		if(typ==0){
			_th_rtn[clenpos_a] = pthread_create( &_th_st_pp[clenpos_a], NULL, kgshell::run_func ,(void*)&_argst[clenpos_a]);
		}
		else if(typ==1){
			_th_rtn[clenpos_a] = pthread_create( &_th_st_pp[clenpos_a], NULL, kgshell::run_writelist ,(void*)&_argst[clenpos_a]);
		}
		else if(typ==2){
			_th_rtn[clenpos_a] = pthread_create( &_th_st_pp[clenpos_a], NULL, kgshell::run_readlist ,(void*)&_argst[clenpos_a]);
		}
		else if(typ==3){
			_th_rtn[clenpos_a] = pthread_create( &_th_st_pp[clenpos_a], NULL, kgshell::run_pyfunc ,(void*)&_argst[clenpos_a]);
		}
	}
	// iterバージョンの終了確認？別スレッドたちあげる?
	return _csvpiped[0];

}


void kgshell::runInit(
	vector<cmdCapselST> &cmds,	
	vector<linkST> & plist
){

	if(!Py_IsInitialized()){
		Py_Initialize();
	}
	if (!PyEval_ThreadsInitialized())	{ 
		PyEval_InitThreads();
	}
	
	char * envStr=getenv("KG_RUN_LIMIT");

	int runlim;
	if ( _runlim == -1){
		if(envStr!=NULL){
			runlim = atoi(envStr);
		}else{
			runlim = KGMOD_RUN_LIMIT;
		}
	}
	else{
		runlim = _runlim;
	}
	if ( runlim <=0 ){
		throw kgError("not valid runlimit");
		return;
	}

	_spblk.blockSplit(runlim,cmds.size(),plist);

	// パラメータ変更		
	vector<linkST>&spedge = _spblk.getsplitEdge();
	for(size_t i=0;i<spedge.size();i++){
		kgstr_t tp = _tempFile.create(false,"kgshellspilt");

		int pos = -1;
		for(size_t j=0;j<cmds[spedge[i].frID].paralist.size();j++){
			if(cmds[spedge[i].frID].paralist[j].find(spedge[i].frTP+"=")==0){
				pos = j; break;
			} 
		} 
		
		if(pos==-1){
			cmds[spedge[i].frID].paralist.push_back(spedge[i].frTP+"="+tp);
		}
		else{
			kgstr_t newpara = cmds[spedge[i].frID].paralist[pos] + "," + tp;
			cmds[spedge[i].frID].paralist[pos]=newpara;
		}

		pos = -1;
		for(size_t j=0;j<cmds[spedge[i].toID].paralist.size();j++){
			if(cmds[spedge[i].toID].paralist[j].find(spedge[i].toTP+"=")==0){
				pos = j;
				break;
			} 
		} 
		if(pos==-1){
			cmds[spedge[i].toID].paralist.push_back(spedge[i].toTP+"="+tp);
		}
		else{
			kgstr_t newpara = cmds[spedge[i].toID].paralist[pos]+","+ tp ;
			cmds[spedge[i].toID].paralist[pos]=newpara;
		}
	}
	return ;
}


int kgshell::runx(
	vector<cmdCapselST> &cmds,	
	vector<linkST> & plist
)
{
	try{
		runInit(cmds,plist);

		for(int iblk=0;iblk<_spblk.getBlksize_M();iblk++){
			runMain(cmds,plist,iblk);
		}
		return 0;

	}catch(kgError& err){
		ostringstream ss;
		ss << "script RUN KGERROR " << err.message(0);
		err_OUTPUT(ss.str());
		runClean();

	}catch (const exception& e) {
		ostringstream ss;
		ss << "script RUN KGERROR " << e.what();
		err_OUTPUT(ss.str());
		runClean();

	}catch(char * er){
		ostringstream ss;
		ss << "script RUN EX ERR " << er;
		err_OUTPUT(ss.str());
		runClean();

	}catch(...){	
		err_OUTPUT("script RUN ERROR UNKNOWN TYPE");
		runClean();
	}
	return 1;
}


kgCSVfld* kgshell::runiter(
	vector<cmdCapselST> &cmds,	
	vector<linkST> & plist
){
	try{

		runInit(cmds,plist);

		for(int iblk=0;iblk<_spblk.getBlksize_M()-1;iblk++){
			runMain(cmds,plist,iblk);
		}

		int itrfd = runiter_SUB(cmds,plist,_spblk.getBlksize_M()-1);
		if(itrfd<0){
			return NULL;
		}

		// データ出力
		_iterrtn = new kgCSVfld;
		_iterrtn->popen(itrfd, &_env,_nfni);
		_iterrtn->read_header();	

		return _iterrtn;

	}catch(kgError& err){
		ostringstream ss;
		ss << "script RUN KGERROR " << err.message(0);
		err_OUTPUT(ss.str());
		runClean();

	}catch (const exception& e) {
		ostringstream ss;
		ss << "script RUN KGERROR " << e.what();
		err_OUTPUT(ss.str());
		runClean();

	}catch(char * er){
		ostringstream ss;
		ss << "script RUN EX ERR " << er;
		err_OUTPUT(ss.str());
		runClean();

	}catch(...){	
		err_OUTPUT("script RUN ERROR UNKNOWN TYPE");
		runClean();
	}

	return NULL;
}


kgCSVkey* kgshell::runkeyiter(
	vector<cmdCapselST> &cmds,	
	vector<linkST> & plist,
	vector<string> & klist
){

	try{

		runInit(cmds,plist);

		for(int iblk=0;iblk<_spblk.getBlksize_M()-1;iblk++){
			runMain(cmds,plist,iblk);
		}

		int itrfd = runiter_SUB(cmds,plist,_spblk.getBlksize_M()-1);

		// データ出力
		_iterrtnk = new kgCSVkey;
 
		_iterrtnk->popen(itrfd, &_env,_nfni);
		_iterrtnk->read_header();	
		kgArgFld fField;
		fField.set(klist, _iterrtnk, false);
		// 入力ファイルにkey項目番号をセットする．
		_iterrtnk->setKey(fField.getNum());

		return _iterrtnk;

	}catch(kgError& err){
		ostringstream ss;
		ss << "script RUN KGERROR " << err.message(0);
		err_OUTPUT(ss.str());
		runClean();

	}catch (const exception& e) {
		ostringstream ss;
		ss << "script RUN KGERROR " << e.what();
		err_OUTPUT(ss.str());
		runClean();

	}catch(char * er){
		ostringstream ss;
		ss << "script RUN EX ERR " << er;
		err_OUTPUT(ss.str());
		runClean();

	}catch(...){	
		err_OUTPUT("script RUN ERROR UNKNOWN TYPE");
		runClean();
	}

	return NULL;

}


int kgshell::getparams( kgstr_t cmdname, PyObject* list){

	kgMod *mod =NULL;

	try{
		if ( _kgmod_map.find(cmdname) == _kgmod_map.end()){
			err_OUTPUT("Not unspport mod " + cmdname);
			return 1;	
		}

		kgArgs newArgs;
		mod	= _kgmod_map.find(cmdname)->second();
		mod->init(newArgs, &_env);
		vector < vector <kgstr_t> > paralist = mod->params();

		for (size_t i=0;i<paralist.size();i++){
			PyObject* tlist = PyList_New(paralist[i].size());
			for(size_t j=0 ;j<paralist[i].size();j++){
				PyList_SetItem(tlist,j,Py_BuildValue("s",paralist[i][j].c_str()));
			}
			PyList_Append(list,tlist);
			Py_DECREF(tlist);
			
		}
		if(mod) delete mod;
		return 0;

	}catch(...){
		err_OUTPUT("UnKnown ERROR IN GET PARAMETER " );
		return 1;	
	}
	return 1;

}